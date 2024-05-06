from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from home.serializers import PeopleSerializer


# Person.objects.all() // all data [1, 2, 3, 4] => datatype is QuerySet.
# Cannot expose queryset in the frontend. 
# Use Serializer to convert this data to Json format, This process is known as serialization.

@api_view(['GET', 'POST']) # Pass methods we are going to use in this function
def index(request):
    
    courses = {
            'course_name' : 'Python',
            'learn' : ['Flask', 'Django', 'Tornado', 'FastApi'],
            'course_provider' : 'Scaler'
            }

    if request.method == "GET":
        print(request.GET.get('search')) # search params from URL
        print("You hit a Get method")
        return Response(courses)

    elif request.method == "POST":
        data = request.data
        print("*********")
        print(data.get('name')) # Or, print(data['name'])
        print("*********")
        print("You hit a Post method")
        return Response(courses)

    elif request.method == "PUT":
        print("You hit a Put method")
        return Response(courses)
    

@api_view(['GET', 'POST'])  # This decorator specifies that this view can handle GET and POST requests.

def person(request):
    # If the request method is GET, retrieve all Person objects and serialize them.
    if request.method == 'GET':
        objs = Person.objects.all()  # Retrieve all Person objects from the database.
        serializer = PeopleSerializer(objs, many=True)  # Serialize the queryset of Person objects. Convert to JSON
        return Response(serializer.data)  # Return serialized data as a response.

    else:
        data = request.data  # Extract data from the request.
        serializer = PeopleSerializer(data=data)  # Initialize serializer with the extracted data.
        # If the data is valid, save it and return serialized data as a response.
        if serializer.is_valid():
            serializer.save()  # Save the validated data.
            return Response(serializer.data)  # Return serialized data as a response.
        
        return Response(serializer.errors)  # If data is not valid, return errors.
