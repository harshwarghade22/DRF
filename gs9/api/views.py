from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# # Create your views here.
# @api_view()
# def helloWorld(request):
#     return Response({'msg':'Hello World'})

@api_view(['GET','POST'])
def helloWorld(request):

    if request.method == 'GET':
        return Response({'msg':'Get req'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Post req','data':request.data})
