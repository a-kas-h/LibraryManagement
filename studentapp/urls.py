from django.contrib import admin
from django.urls import path
from studentapp import views

urlpatterns = [
     path('',views.index,name="index"),
     path('index.html',views.index,name="studentapp"),
     path('student.html',views.student,name="student"),
     path('deletestd/<int:id>',views.deletestd),
     path('bookmaster.html',views.bookmaster,name="bookmaster"),
     path('deleteb/<int:id>',views.deleteb),
     path("bookissuemaster.html",views.bookissuetemp,name="bookissuetemp"),
     path('deletebook/<int:id>',views.deletebook),
     path("addbookissuedata/",views.addbookissuedata,name="addbookissuedata"),
     #path('bedit/<int:id>',views.bedit),
     path('bupdate/<int:id>',views.bupdate),
     path("issuedbook.html",views.issuedbook,name="issuedbook"),
     path("finecheck.html",views.finecheck,name="finecheck"),
      path("report.html",views.report,name="report"),
]