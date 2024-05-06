from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person,
        fields = '__all__'   # => Serialize all fields


        # exclude = ['name']    => Write all the fields you want to exclude/not want to serialize
        # fields = ['name', 'age']  => Serialize these particular fields