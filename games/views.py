from django.shortcuts import render
from .models import Game, Studio
from .serializers import GameSerializer
from django.http import JsonResponse


def games_list(request):
    game_lst = Game.objects.all()
    serializer = GameSerializer(game_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)
