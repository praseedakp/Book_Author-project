from django import forms

#adminloginform:
class adminform(forms.Form):
    adminuname=forms.CharField(max_length=50)
    adminpassw=forms.CharField(max_length=50)



#authorform:
class authorform(forms.Form):
    authname=forms.CharField(max_length=100)
    uname=forms.CharField(max_length=100)
    email=forms.EmailField()




##bookform:
class bookform(forms.Form):
    bookna=forms.CharField(max_length=100)
    authorname=forms.CharField(max_length=100)