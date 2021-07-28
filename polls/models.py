from django.db import models

# Create your models here.
emp_statuses = (('ACTIVE', "Активен"), ("VACATION", "Отпуск"), ("FIRED", "Уволен"))


class Position(models.Model):
    name = models.CharField("Название позиции", max_length=50)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField("ФИО", max_length=100)
    position = models.ForeignKey(Position, verbose_name="Позиция", on_delete=models.DO_NOTHING)
    status = models.CharField("Статус", max_length=50, choices=emp_statuses)

    def __str__(self):
        return self.position
