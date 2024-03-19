from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import bookAPIModelSerializer
from .models import BooksAPIModel

@api_view(['GET','POST'])
def booksListAPI(request):
    if request.method == "GET":
        query = BooksAPIModel.objects.all()
        serializer = bookAPIModelSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        query = request.data
        serializer = bookAPIModelSerializer(data=query)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PATCH','PUT',"DELETE"])
def bookDetailAPI(request,id):
    query = BooksAPIModel.objects.get(id=id)
    if request.method == "GET":
        serializer = bookAPIModelSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = bookAPIModelSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PATCH":
        serializer = bookAPIModelSerializer(query,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        query.delete()
        return Response("Data Deleted Successfully",status=status.HTTP_204_NO_CONTENT)

