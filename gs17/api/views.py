from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    def update(self,request,pk=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
    def destroy(self,request,pk=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Student deleted'})
    

    def retrieve(self,request,pk=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu)
        return Response(serializer.data)
    
    