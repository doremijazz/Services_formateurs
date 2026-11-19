from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Trainer(models.Model):
    initials = models.CharField(max_length=5)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    start_date = models.DateField()

    def id_ir(self, date):
        pass

    def nb_services(self, strat, end):
        pass


class Service(models.Model):
    date = models.DateField()
    type = models.IntegerField()
    status = models.IntegerField()

    def to_affected_services(self, formateur):
        pass

    def delete_affectation(self):
        pass

class ClasseShedule(models.Model):
    weekday = models.IntegerField()
    period = models.IntegerField()

class Direction(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def generate_planning(self):
        pass

class Resquest(models.Model):
    type = models.IntegerField()
    days = models.IntegerField()
    date = models.DateTimeField()
    type_service = models.IntegerField()




