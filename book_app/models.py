from django.db import models


#authormodel:
class authormodel(models.Model):
    authname=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.authname




#bookmodel:
class bookmodel(models.Model):
    bookna=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.bookna