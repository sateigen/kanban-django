from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


from .models import Board, Task, Ticket
from .serializers import BoardSerializer, TaskSerializer, TicketSerializer
from rest_framework import viewsets


def index(request):
    return render(request, 'board/index.html')


@login_required
def all_boards(request):
    user = request.user

    if request.POST:
        name = request.POST['name']
        b = Board(name=name)
        b.save()
        b.user.add(user)
        b.save()

    boards = Board.objects.filter(user=user)
    context = {
        'boards': boards
    }
    return render(request, 'board/all_boards.html', context)


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
    if request.POST:
        name = request.POST['name']
        description = request.POST['description']
        t = Ticket(name=name, description=description, board=board)
        t.save()
    context = {
        'board': board
    }
    return render(request, 'board/board.html', context)


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/all_boards/')
    else:
        return render(request, 'registration/login.html')


def signout(request):
    logout(request)
    return render(request, 'registration/logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form['username'].value(), password=form['password1'].value())
            if new_user is not None:
                login(request, new_user)
                return HttpResponseRedirect('/all_boards/')
            # return HttpResponseRedirect('/all_boards/')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
