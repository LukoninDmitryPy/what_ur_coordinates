import random
import requests

from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from cadastral.models import Coordinates, Result
from .serializers import CoordinatesSerializer, ResultSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    """Вьюсет для координат"""

    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class ResultViewSet(viewsets.ModelViewSet):
    """Вьюсет для результата"""

    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    @action(detail=False, methods=['post'],)
    def boolea(self, request):
        result = random.choice([True, False])
        res = {'coordinates': request.data['coordinates'], 't_or_f': result}
        serializer = ResultSerializer(data=res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'],)
    def history(self, request):
        recently_check = Result.objects.all().order_by('-id')
        serializer = ResultSerializer(recently_check, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def status_service(request):
    """Получение статуса сервера"""
    try:
        response = requests.head('https://545ithub.com')
        response.status_code == status.HTTP_200_OK
        message = 'Succesful'
        return Response(message, status=status.HTTP_200_OK)
    except requests.ConnectionError as r:
        error = f'Сервер не доступен! {r}'
        return Response(error)

