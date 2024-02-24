from django.db import models

# Create your models here.




class catagori(models.Model):
    catagori_name = models.TextField()

    def __str__(self) -> str:
        return self.catagori_name

class product(models.Model):
    product_name = models.TextField()
    product_dis = models.TextField()
    image = models.ImageField(null=True)
    price =  models.FloatField(null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)
    catagories = models.ForeignKey(catagori, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name
    


class aboutcont(models.Model):
    about_dis = models.TextField()
    about_title = models.TextField()
    image = models.ImageField(null=True)


    def __str__(self) -> str:
        return self.about_dis
    