from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board, Task, Ticket
from .serializers import BoardSerializer, TaskSerializer, TicketSerializer
from rest_framework import viewsets


@login_required
def index(request):
    user = request.user
    boards = Board.objects.filter(user=user)
    context = {
        'boards': boards
    }
    return render(request, 'board/index.html', context)


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

@login_required
def board_detail(request, board_id):
    board = Board.objects.get(pk=board_id)
    context = {
        'board': board
    }
    return render(request, 'board/board.html', context)
