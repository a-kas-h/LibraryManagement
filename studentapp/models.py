from django.db import connection
from django.db import models
from datetime import datetime

# student add 
class studentadd(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    class Meta:
        db_table="student"
        managed = False
#book add
class bookadd(models.Model):
    bookname=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    serialno=models.IntegerField()
    edition=models.CharField(max_length=100)
    fineamt=models.IntegerField()
    class Meta:
        db_table="bookmaster"
        managed = False
class bookissuetempd(models.Model):
    bookname=models.CharField(max_length=100)
    issueuptodate=models.DateField()
    class Meta:
        db_table="bookissuetemp"
        managed = False
class bookissuemaster(models.Model):
    #  id=models.IntegerField(primary_key=True)
     smid=models.CharField(max_length=100)
     totalnobook=models.IntegerField()
     datetime=models.DateTimeField(default=datetime.now(), blank=True)
     class Meta:
        db_table="bookissuemaster"
        managed = False
class bookissuemastershow(models.Model):
    #  id=models.IntegerField(primary_key=True)
     smid=models.CharField(max_length=100)
     totalnobook=models.IntegerField()
     datetime=models.DateField()
     class Meta:
        db_table="bookissuemaster"
        managed = False
class bookissuedetails(models.Model):
    # bookissueid=models.ForeignKey(bookissuemaster, on_delete=models.CASCADE)
    bookissueid=models.CharField(max_length=100)
    bookmasterid=models.CharField(max_length=100)
    issueuptodate=models.DateField()
    class Meta:
        db_table="bookissuedetails"
        managed = False
class bookissuedetailsupdate(models.Model):
    bookissueid=models.ForeignKey(bookissuemaster, on_delete=models.CASCADE)
    bookissueid=models.CharField(max_length=100)
    bookmasterid=models.CharField(max_length=100)
    issueuptodate=models.DateField()
    returnstatus=models.IntegerField()
    returndate=models.DateField()
    fineamt=models.IntegerField()
    class Meta:
        db_table="bookissuedetails"
        managed = False
class returndateupdate(models.Model):
    returndate=models.DateField()
    returnstatus=models.IntegerField(default=1)
    class Meta:
        db_table="bookissuedetails"
        managed = False
class returndateupdate1(models.Model):
    fineamt=models.IntegerField()
    class Meta:
        db_table="bookissuedetails"
        managed = False
        