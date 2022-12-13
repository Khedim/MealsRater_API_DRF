from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_rating(self):
        return len(Rating.objects.filter(meal=self))

    def avg_rating(self):
        pass
        s = 0
        r = Rating.objects.filter(meal=self)
        for x in r:
            s += x.stars
        return "%.1f" % (s / len(r)) if s else 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return str(self.meal)

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)