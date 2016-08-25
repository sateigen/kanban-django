from rest_framework import serializers
from board.models import Board, Status, Task, Ticket


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('progress', 'task')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('description', 'points')


class TicketSerializer(serializers.ModelSerializer):
    task_set = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'name', 'description', 'task_set')


class BoardSerializer(serializers.ModelSerializer):
    ticket_set = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('name', 'user', 'ticket_set')

    def create(self, data):
        board = Board.objects.create(**data)
        return board
