from django.db import models



# Create your models here.

class HDData(models.Model):
    class Shape(models.IntegerChoices):
        CIRCLE = 0, "Circle"
        POINT = 1, "Point"
        LINE = 2, "Line"
        TRIANGLE = 3, "Triangle"
        SQUARE = 4, "Square"

    x = models.IntegerField()
    y = models.IntegerField()
    shape = models.PositiveSmallIntegerField(choices=Shape.choices, default=Shape.CIRCLE)

    def __str__(self):
        return f"{self.get_shape_display()} : ({self.x}, {self.y})"