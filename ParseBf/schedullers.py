import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ParseBf.ParseBf.settings")
django.setup()

from django_q.tasks import schedule


class Scheduller:
    # def __init__(self):
        # self.bot = Bot()

    def go_sched(self):
        schedule('hi', schedule_type='I', minutes=1, repeats=-1)


