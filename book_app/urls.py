from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("author_view",author_view,basename='author_view')
router.register("book_view",book_view,basename='book_view')

urlpatterns=[
    path('adminlogin/',adminlogin),
    path('authreg/',authreg),
    path('authordisp/',authordisp),
    path('bookreg/',bookreg),
    path('bookdisp/',bookdisp),
    path('authoredit/<int:id>',authedit),
    path('bookedit/<int:id>',bookedit),
    path('authdetails/<int:id>',authdetails),
    path('logout/',logout_view),

    ]+(router.urls)
