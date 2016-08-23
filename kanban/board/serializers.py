from rest_framework import serializers
from board.models import Board, Status, Task, Ticket


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'user')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('progress', 'task')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('ticket', 'description', 'points')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('name', 'description', 'board')
