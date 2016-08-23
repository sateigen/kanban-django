from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)

    def __str__(self):
        return "Board Name: {} User: {}".format(self.name, self.user)


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    board = models.ForeignKey(Board)


class Task(models.Model):
    description = models.TextField(null=True, blank=True)
    ticket = models.ForeignKey(Ticket)
    points = models.IntegerField(default=1)


class Status(models.Model):
    BACKLOG = 'BACKLOG'
    INPROGRESS = 'INPROGRESS'
    DONE = 'DONE'
    BLOCKED = 'BLOCKED'
    CUSTOM = 'CUSTOM'
    STATUS_CHOICES = (
        (BACKLOG, 'Backlog'),
        (INPROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (BLOCKED, 'Blocked'),
        (CUSTOM, 'Custom')
    )

    progress = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=BACKLOG
    )
    task = models.OneToOneField(Task)
