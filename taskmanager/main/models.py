from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length=150)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Задача"
        verbose_name_plural="Задачи"

class Product(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to='img/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


