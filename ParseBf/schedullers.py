import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ParseBf.settings")
django.setup()

from django_q.tasks import schedule


class Scheduller:
    # def __init__(self):
        # self.bot = Bot()
    @staticmethod
    def go_sched():
        schedule('browser_class.Tst.hi', schedule_type='I', minutes=1, repeats=-1)


Scheduller.go_sched()