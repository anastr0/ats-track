from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# DONE : Create a table called Candidate with columns: [Name, Age, Gender, Email, Phone number]
# TODO : Create api endpoints to: create, update and delete a candidate. 
# TODO : Also create an api endpoint to Search candidates (Explained in detail below). Searching should work on candidates name and should return results sorted based on relevancy. Relevancy is defined as the number of words in the search query that can be found in candidates name.

# Create your views here.
@api_view(['GET'])
def getData(request):
    return Response()


@api_view(['POST'])
def postData(request):
    return Response()
