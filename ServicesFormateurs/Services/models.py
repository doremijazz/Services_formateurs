from django.contrib.auth.models import User
from django.db import models


class ServiceType(models.IntegerChoices):
    MORNING = 1, "Levé"
    LUNCH = 2, "Midi"
    EVENING = 3, "Veillée"


class PlanningStatus(models.IntegerChoices):
    En_cours = 1, "En cours"
    Finished = 2, "Finalisé"


class ServiceStatus(models.IntegerChoices):
    En_attente = 1, "En attente"
    Pourvu = 2, "Pourvu"


class RequestType(models.IntegerChoices):
    Souhait = 1, "Souhait"
    Indisponible = 2, "Indisponible"


class Trainer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="trainer"
    )
    initials = models.CharField(max_length=5)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    start_date = models.DateField()

    def id_ir(self, date):
        pass

    def nb_services(self, start, end):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SchoolYear(models.Model):
    label = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()

    def contains(self, date):
        return self.start <= date <= self.end

    def __str__(self):
        return self.label


class Planning(models.Model):
    generation_date = models.DateField()
    statut = models.IntegerField(choices=PlanningStatus.choices)

    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        related_name="plannings"
    )

    def generated(self):
        pass


class Service(models.Model):
    date = models.DateField()



    type = models.IntegerField(choices=ServiceType.choices)
    status = models.IntegerField(choices=ServiceStatus.choices)

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="services"
    )

    planning = models.ForeignKey(
        Planning,
        on_delete=models.CASCADE,
        related_name="services"
    )

    def to_affect(self, trainer):
        self.trainer = trainer
        self.save()

    def delete_affectation(self):
        self.trainer = None
        self.save()


class ClasseSchedule(models.Model):
    weekday = models.IntegerField()
    period = models.IntegerField()
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="class_schedules"
    )


class Direction(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="direction"
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def generate_planning(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Request(models.Model):
    type = models.IntegerField(choices=RequestType.choices)
    days = models.IntegerField()
    date = models.DateTimeField()
    type_service = models.IntegerField(choices=ServiceType.choices)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="requests"
    )


class HolidayPeriod(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        related_name="holiday_periods"
    )

    def contains(self, date):
        return self.start_date <= date <= self.end_date

    def __str__(self):
        return self.name
