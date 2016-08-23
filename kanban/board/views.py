from django.shortcuts import render
from .models import Board, Task, Ticket
from .serializers import BoardSerializer, TaskSerializer, TicketSerializer
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html')


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
