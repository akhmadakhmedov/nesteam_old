from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from .models import *
from .serializers import *


#def games_list(request):
#    game_lst = Game.objects.all()
#    serializer = GameSerializer(game_lst, many=True)
#    data = serializer.data
#    return JsonResponse(data, safe=False)

class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


#class CreateGameAPIView(CreateAPIView):
#    queryset = Game.objects.all()
#    serializer_class = GameSerializer

class GameView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer