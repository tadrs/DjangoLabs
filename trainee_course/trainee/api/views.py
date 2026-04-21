from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics
from ..models import Trainee
from .serializer import TraineeSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def trainee_list(request):
    trainees = Trainee.objects.all()
    serializer = TraineeSerializer(trainees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def trainee_detail(request, ID):
    try:
        trainee = Trainee.objects.get(pk=ID)
    except Trainee.DoesNotExist:
        return Response(status=404)

    serializer = TraineeSerializer(trainee)
    return Response(serializer.data)


class TraineeCreate(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


class TraineeUpdate(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, id):
        try:
            trainee = Trainee.objects.get(pk=id)
        except Trainee.DoesNotExist:
            return Response(status=404)

        serializer = TraineeSerializer(trainee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TraineeDelete(generics.DestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        try:
            trainee = Trainee.objects.get(pk=id)
        except Trainee.DoesNotExist:
            return Response(status=404)

        trainee.delete()
        return Response(status=204)
