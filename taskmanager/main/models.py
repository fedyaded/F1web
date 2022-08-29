from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length=150)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Задача"
        verbose_name_plural="Задачи"

class Project(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to='img/')



