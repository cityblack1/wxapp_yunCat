from feedback.models import FeedBack, Contact
from feedback.serializers import FeedBackSerializer, ContactSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from feedback.permissions import IsAdminOrReadOnly


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    #
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsAdminOrReadOnly,)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)


class FeedBackList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    #
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FeedBackDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class ContactList(APIView):
#     def get(self, request, format=None):
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ContactSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ContactDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(id=pk)
#         except Contact.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         contact = self.get_object(pk=pk)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

