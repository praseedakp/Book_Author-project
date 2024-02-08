from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth import logout

from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage





# admin login:
def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['adminuname']
            password=a.cleaned_data['adminpassw']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return HttpResponse("login success")

            else:
                return HttpResponse("Login failed")

    return render(request,'adminloginpage.html')





#author registration:
def authreg(request):
    if request.method=='POST':
        k=authorform(request.POST)
        if k.is_valid():
            aname=k.cleaned_data['authname']
            uname=k.cleaned_data['uname']
            em=k.cleaned_data['email']
            m=authormodel(authname=aname,uname=uname,email=em)
            m.save()
            return redirect(authordisp)
        else:
            return HttpResponse("failed")

    return render(request,'authorreg.html')




#bookcreation:
def bookreg(request):
    if request.method=='POST':
        b=bookform(request.POST)
        if b.is_valid():
            bna=b.cleaned_data['bookna']
            aname=b.cleaned_data['authorname']
            c=bookmodel(bookna=bna,authorname=aname)
            c.save()
            return redirect(bookdisp)
        else:
            return HttpResponse("failed")

    return render(request,'bookreg.html')

#author display:
def authordisp(request):
    a=authormodel.objects.all()
    count_auth=authormodel.objects.all().count()
    count_book=bookmodel.objects.all().count()
    u=User.objects.all()
    a1=authormodel.objects.all().order_by("id")
    paginator=Paginator(a1,1)
    page=request.GET.get('page',1)
    ay=paginator.get_page(page)
    return render(request,'authordisplay.html',{'a':a,'count_auth':count_auth,'count_book':count_book,'u':u,'ay':ay})




#books display:
def bookdisp(request):
    s=bookmodel.objects.all()
    count_auth=authormodel.objects.all().count()
    count_book=bookmodel.objects.all().count()
    u=User.objects.all()
    s1=bookmodel.objects.all().order_by("id")
    paginator=Paginator(s1,1)
    page=request.GET.get('page',1)
    bt=paginator.get_page(page)
    return render(request,'bookdisplay.html',{'s':s,'count_auth':count_auth,'count_book':count_book,'u':u,'bt':bt})


#author edit:
def authedit(request,id):
    a=authormodel.objects.get(id=id)
    if request.method=='POST':
        a.authname=request.POST.get('authname')
        a.uname=request.POST.get('uname')
        a.email=request.POST.get('email')
        a.save()
        return redirect(authordisp)
    return render(request,'authoredit.html',{'a':a})



#book edit:
def bookedit(request,id):
    a=bookmodel.objects.get(id=id)
    if request.method=='POST':
        a.bookna=request.POST.get('bookna')
        a.authorname=request.POST.get('authorname')
        a.save()
        return redirect(bookdisp)
    return render(request,'bookedit.html',{'a':a})



#detail view of author and list view of books:
def authdetails(request,id):
    a=authormodel.objects.get(id=id)
    h=bookmodel.objects.all()
    u=User.objects.all()
    h1=bookmodel.objects.all().order_by("id")
    paginator=Paginator(h1,1)
    page=request.GET.get('page',1)
    dy=paginator.get_page(page)
    return render(request,'detaildisplay.html',{'a':a,'h':h,'u':u,'dy':dy})


#logout:
def logout_view(request):
    logout(request)
    return redirect(adminlogin)


# ----------------------------------------

#restapi authorview
class author_view(viewsets.ModelViewSet):
    serializer_class = authorserializer
    queryset = authormodel.objects.all()

#keysearch using authorname
    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        author=authormodel.objects.filter(authname=params['pk'])
        serializer=authorserializer(author,many=True)
        return Response(serializer.data)




#Restapi bookview:

class book_view(viewsets.ModelViewSet):
    serializer_class = bookserializer
    queryset = bookmodel.objects.all()

    # keysearch using bookname
    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        book=bookmodel.objects.filter(bookna=params['pk'])
        serializer=bookserializer(book,many=True)
        return Response(serializer.data)

# --------------------------------------
