from django.db import models


class EventGamer(models.Model):

    game_type = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event_type = models.ForeignKey("Event", on_delete=models.CASCADE)