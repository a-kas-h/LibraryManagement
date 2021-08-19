from django.shortcuts import  redirect,render,HttpResponse
from studentapp.models import *
from django.contrib import messages
from datetime import datetime
# import datetime
from datetime import date
import random
# Create your views here.
def index(request):
     return render(request,'index.html')
#for studdent
def student(request):
     show=studentadd.objects.all()
     if request.method=="POST":
        if request.POST.get('name'):
            x = random.randint(0,5000000)
            saverecord=studentadd()
            saverecord.name=request.POST.get('name')
            saverecord.rollno=x
            saverecord.fname=request.POST.get('fname')
            saverecord.mname=request.POST.get('mname')
            saverecord.mobileno=request.POST.get('mobileno')
            saverecord.email=request.POST.get('email')
            saverecord.age=request.POST.get('age')
            saverecord.save()
            messages.success(request,"student added")
            show=studentadd.objects.all()
            return render(request,"student.html",{'show':show})
     else:
            return render(request,"student.html",{'show':show}) 
def deletestd(request,id):
    user=studentadd.objects.get(id=id)
    user.delete()
    return redirect('/student.html')
#book master
def bookmaster(request):
     show=bookadd.objects.all()
     if request.method=="POST":
        if request.POST.get('bookname'):
            saverecord=bookadd()
            saverecord.bookname=request.POST.get('bookname')
            saverecord.publication=request.POST.get('publication')
            saverecord.serialno=request.POST.get('serialno')
            saverecord.edition=request.POST.get('edition')
            saverecord.fineamt=request.POST.get('fineamt')
            saverecord.save()
            messages.success(request,"book added")
            show=bookadd.objects.all()
            return render(request,"bookmaster.html",{'show':show})
     else:
            return render(request,"bookmaster.html",{'show':show}) 
def deleteb(request,id):
    user=bookadd.objects.get(id=id)
    user.delete()
    return redirect('/bookmaster.html')
def bookissuetemp(request):
     show=bookadd.objects.all()
     bdet=bookissuetempd.objects.all()
     j=0
     count=0
     i=0
     for h in bdet:
       j=j+h.id
       count+=1
     i=count
     SDetails=studentadd.objects.all()
     if request.method=="POST":
        if request.POST.get('bookmasterid') and request.POST.get('issueuptodate'):
          saver=bookissuetempd()
          saver.bookname=request.POST.get('bookmasterid')
          saver.issueuptodate=request.POST.get('issueuptodate')
          saver.save()
          show=bookadd.objects.all()
          bdet=bookissuetempd.objects.all()
          j=0
          count=0
          for h in bdet:
               j=j+h.id
               count+=1
          i=str(count)
          SDetails=studentadd.objects.all()
          return render(request,"bookissuemaster.html",{'show':show,'bdet':bdet,'SDetails':SDetails,'i':str(i)})
     else:
          return render(request,"bookissuemaster.html",{'show':show,'bdet':bdet,'SDetails':SDetails,'i':str(i)}) 
def deletebook(request,id):
    user=bookissuetempd.objects.get(id=id)
    user.delete()
    return redirect('/bookissuemaster.html')
def addbookissuedata(request):
    if request.method=="POST":
         if request.POST.get('name'):
               d=request.POST.get('name')
               sd=bookissuemaster()
               sd.smid=request.POST.get('name')
               sd.totalnobook=request.POST.get('totalbook')
               sd.save()
               saverecord=bookissuetempd.objects.all()
               for x in saverecord:
                    saverecord=bookissuedetails()
                    saverecord.bookmasterid=x.bookname
                    saverecord.issueuptodate=x.issueuptodate
                    saverecord.bookissueid=d
                    saverecord.save()
               bookissuetempd.objects.all().delete()
               return redirect('/bookissuemaster.html')
         else:
               return render(request,"/bookissuemaster.html")
# def bedit(request,id):
#     user=bookissuedetails.objects.get(id=id)
#     return render(request,'bedit.html',{'sd':user,})
def bupdate(request,id):
#     user=bookissuedetailsupdate.objects.get(id=id)
#     saverecord.bookmasterid=request.POST.get('bookmasterid')
#     saverecord.returnstatus=request.POST.get('returnstatus')
#     saverecord.issueuptodate=request.POST.get('issueuptodate')
#     saverecord.fineamt=request.POST.get('fineamt')
    saverecord=returndateupdate(id)
    saverecord.returndate=request.POST.get('returndate')
    saverecord.save()
    saverecord=returndateupdate1(id)
    bookdtl=bookissuedetailsupdate.objects.filter(pk=id)
    for j in bookdtl:
        h=j.returndate-j.issueuptodate
        print(h)
        q=h.days
        print(q)
        k=bookadd.objects.raw('select id,bookname,fineamt from bookmaster where bookname="'+j.bookmasterid+'"')
        for l in k:
          print(l.fineamt)
          d=q*l.fineamt
          print(d)
    saverecord.fineamt=d      
    saverecord.save()
    return redirect('/issuedbook.html',{'d':d})
def issuedbook(request):
     pdm=bookissuemastershow.objects.all()
     bdm=bookissuedetailsupdate.objects.all()        
     searchfine=bookadd.objects.all()
     return render(request,"issuedbook.html",{'pdm':pdm,'bdm':bdm,'searchfine':searchfine})

def finecheck(request):
     h=bookissuedetailsupdate.objects.all()
     searchresult=bookadd.objects.all()
     return render(request,'finecheck.html',{'h':h,'d':searchresult})
# def finecheck(request):
#      # searchresult=bookissuemastershow.objects.raw('select datatime from bookissuemaster')
#      h=bookissuedetailsupdate.objects.raw('select id,bookmasterid,issueuptodate,returndate from bookissuedetails')
#      # for q,j in zip(h,searchresult) :
#      for q in h:
#       b=q.bookmasterid
#       searchresult=bookadd.objects.raw('select id,fineamt,bookname from bookmaster where bookname = "'+b+'"')
#       f=[q.returndate-q.issueuptodate]
#       c=f*searchresult.id
#      c=[str(f)]
#      print(c)
#      return render(request,'finecheck.html',{'c':c})
#for report 
def report(request):
    if request.method=="POST":
      fromdate=request.POST.get('fromdate')
      todate=request.POST.get('todate')
      searchresult=bookissuedetailsupdate.objects.raw('select id,bookissueid,bookmasterid,issueuptodate from bookissuedetails WHERE issueuptodate BETWEEN "'+str(fromdate)+'" AND "'+str(todate)+'"')
      return render(request,'report.html',{"data":searchresult})
    else:
      return render(request,'report.html')