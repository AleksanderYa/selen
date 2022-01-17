import os
import django


class Scheduller:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ParseBf.settings")
    django.setup()
    from django_q.tasks import schedule as schedule

    @staticmethod
    def go_sched():
        Scheduller.schedule('browser_class.Tsts.go', schedule_type='I', minutes=1, repeats=-1)

    @staticmethod
    def go_sched_hi():
        Scheduller.schedule('browser_class.Tst.hi', schedule_type='I', minutes=1, repeats=-1)

Scheduller.go_sched()