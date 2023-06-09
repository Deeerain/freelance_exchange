from replays import models


def create_replay(**kwargs):
    models.Replay.objects.create(**kwargs)