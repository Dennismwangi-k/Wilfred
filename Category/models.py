from django.db import models

class Category(models.Model):
    RECYCLABLE_CHOICES = [
        ("glass", "Glass"),
        ("plastic", "Plastic"),
        ("paper", "Paper"),
        ("metal", "Metal"),
        ("batteries", "Batteries"),
    ]

    ORGANIC_CHOICES = [
       
        ("food_waste", "Food_waste"),
        ("compost", "Compost"),
        ("animal waste", "Animal waste"),
    ]
    recyclable = models.CharField(choices=RECYCLABLE_CHOICES, max_length=20)
    organic = models.CharField(choices=ORGANIC_CHOICES, max_length=20)
    def __str__(self):
        return self.get_recyclable_display() if self.recyclable else self.get_organic_display()


   




 















