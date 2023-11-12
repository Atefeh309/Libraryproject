from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .serializers import userserializers, bookserializers, reserveserializers
from rest_framework import viewsets
from .models import UserProfile, book, reserve


# Create your views here.
class userviewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = userserializers


class bookviewset(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = bookserializers


class reservesviewset(viewsets.ModelViewSet):
    queryset = reserve.objects.all()
    serializer_class = reserveserializers

    def create(self, request, *args, **kwargs):
        u = UserProfile.objects.get(id=int(request.data['user_id']))
        b = book.objects.get(id=int(request.data['book_id']))
        request.data.pop('user_id')
        request.data.pop('book_id')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            reserv = serializer.create(validated_data=request.data)
            reserv.book_name = b
            reserv.transferee = u
            reserv.save()
            s = self.serializer_class(reserv)
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def list(self, request, *args, **kwargs):
        book_list = []
        r = reserve.objects.all()
        for book in r:
            if book.book_name:
                book_list.append(book.book_name)
        s = bookserializers(book_list, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        r = reserve.objects.get(id=int(request.data['reserve_id']))
        u = UserProfile.objects.get(id=int(request.data['user_id']))
        b = book.objects.get(id=int(request.data['book_id']))
        request.data.pop('reserve_id')
        request.data.pop('user_id')
        request.data.pop('book_id')
        r.transferee = u
        r.book_name = b
        r.save()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.update(instance=r, validated_data=request.data)
            s = self.serializer_class(r)
            return Response(s.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        r = reserve.objects.get(id=int(request.data['reserve_id']))
        request.data.pop('reserve_id')
        if r:
            r.trash=True
            r.save()
            massage="deleted is done"
            return Response({"massage":massage},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

        

        