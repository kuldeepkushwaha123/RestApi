from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import Student_serializer
from rest_framework.response import Response
from .models import Student


# Create your views here.
@api_view(['GET'])
def show(request):
    data = Student.objects.all()
    serializer = Student_serializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def display_message(request):
    serializer = Student_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('form invailid')


@api_view(['GET'])
def show_one(request, id):
    try:
        data = Student.objects.filter(id=id)
        if data:

            serializer = Student_serializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response('Record not found')
    except:
        return Response("Something went wrong!!")


@api_view(['PUT'])
def studentUpdate(request, id):
    try:
        record = Student.objects.get(id=id)
        serializer = Student_serializer(record, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': "Record has been updated", 'data': request.data})
        else:
            return Response('Invailed serializer!')
    except:
        return Response('data not found')


@api_view(['DELETE'])
def delStudent(request, id):
    data = Student.objects.filter(id=id)
    if data:
        data.delete()
        return Response("data has been deleted!!")
    else:
        return Response("Record is not found!")
