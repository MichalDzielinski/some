from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Log


@receiver(post_save, sender=Log)
def calculate_log_time_and_update_total_task_time(sender, instance, created, **kwargs):
    if instance.time_end:
        log_time = instance.time_end - instance.time_start
        # instance.time = log_time
        # instance.save()
        Log.objects.filter(pk=instance.pk).update(time=log_time, is_finished=True)

        instance.task.total_time += log_time
        instance.task.save()
