from django.db import models

# Create your models here.

class Worker(models.Model):
    name =models.CharField(verbose_name="氏名",max_length=20)
    year =models.DateField(verbose_name="生年月日")

    class Meta:
        verbose_name_plural = "労働者"

    def __str__(self):
        return self.name

class Attendance(models.Model):
    worker = models.ForeignKey(Worker,verbose_name="労働者",on_delete=models.CASCADE)
    date = models.DateField(verbose_name="日付")
    start_time= models.TimeField(verbose_name="出勤時間")
    finish_time=models.TimeField(verbose_name="退勤時間")

    class Meta:
        verbose_name_plural = "勤怠"

    def __str__(self):
        return str(self.date) +" : "+ str(self.woker)