from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'   # => Serialize all fields
        # exclude = ['name']    => Write all the fields you want to exclude/not want to serialize
        # fields = ['name', 'age']  # => Serialize these particular fields

    def validate(self, data):
        special_characters = '[!@#$%^&*(),.?":{}|<>]'

        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name cannot contain any special characters")

        if data['age'] < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        
        return data


    # def validate_age(self, age):
    #      print(age)
    #      return age

        
        