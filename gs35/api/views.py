from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[SearchFilter]
    # search_fields=['city']
    # search_fields=['name','city']    -> Search with name or city
    # search_fields=['^name']    # ^ -> Start with  -> Search only with name
    # search_fields=['name$']    # $ -> End with  -> Search only with name
    # search_fields=['name__icontains']    # icontains -> Case insensitive search  -> Search with name containing any letter in any case
    # search_fields=['name__iexact']    # iexact -> Case insensitive exact match  -> Search only with exact name
    # search_fields=['city__in']    # in -> Multiple search  -> Search in multiple cities
    # search_fields=['city__startswith']    # startswith -> Starts with  -> Search in cities starting with a given letter
    # search_fields=['city__endswith']    # endswith -> Ends with  -> Search in cities ending with a given letter
    # search_fields=['city__range']    # range -> Between a range  -> Search in cities between two given ranges
    # search_fields=['city__regex']    # regex -> Regular expression  -> Search in cities matching a given regular expression
    # search_fields=['city__iregex']    # iregex -> Case insensitive regular expression  -> Search in cities matching a given regular expression in any case
    # search_fields=['city__gt']    # gt -> Greater than  -> Search in cities greater than a given value
    # search_fields=['city__gte']    # gte -> Greater than or equal to  -> Search in cities greater than or equal to a given value
    # search_fields=['city__lt']    # lt -> Less than  -> Search in cities less than a given value
    # search_fields=['city__lte']    # lte -> Less than or equal to  -> Search in cities less than or equal to a given value
    # search_fields=['city__isnull']    # isnull -> Is null  -> Search in cities with null value
    # search_fields=['city__isnull']    # isnull -> Is not null  -> Search in cities with non-null value
    # search_fields=['city__contains']    # contains -> Contains  -> Search in cities containing a given value
    # search_fields=['city__icontains']    # icontains -> Case insensitive contains  -> Search in cities containing a given value in any case
    # search_fields=['city__startswith']    # startswith -> Starts with  -> Search in cities starting with a given letter
    # search_fields=['city__endswith']    # endswith -> Ends with  -> Search in cities ending with a given letter



 
