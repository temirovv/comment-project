from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment, People
from .serializers import CommentSerializer, PeopleSerializer


class CommentAPIView(APIView):
    def get(self, request): 
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'xabar': "kiritilgan malumotlar xato"})
        


class PeopleAPIView(APIView):
    def get(self, request):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass