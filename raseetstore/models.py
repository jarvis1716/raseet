from django.db import models


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class sub_category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mrp = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    manufacturer = models.CharField(max_length=150, null=False, default='')
    Salt_composition = models.CharField(max_length=200, null=False, default='')

    def __str__(self):
        return self.name


class about_product(models.Model):
    drug_info = models.TextField()
    when_to_use = models.CharField(max_length=200)
    how_to_use = models.TextField()
    benefits = models.TextField()
    side_effects = models.TextField()
