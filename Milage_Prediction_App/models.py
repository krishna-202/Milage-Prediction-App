from django.db import models

class MilagePredictionModel(models.Model):
    cylinders=models.IntegerField()
    displacement=models.IntegerField()
    horsepower=models.IntegerField()
    weight=models.IntegerField()
    acceleration=models.IntegerField()
    model_year=models.IntegerField()
    origin=models.IntegerField()
    predicted_value=models.IntegerField(default=18)



# Create your models here.
