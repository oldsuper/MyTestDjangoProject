from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)
    # age=models.IntegerField()
    def insert(self,id,name):
        Test.objects.create(id=id,name=name)
    def get(self,id=None,name=None):
        if len(id.strip())==0 and len(name.strip())==0:
            return Test.objects.all()
        else:
            if len(id.strip())!=0 and len(name.strip())!=0:
                return Test.objects.filter(id=id,name=name)
            if len(id.strip())!=0:
                return Test.objects.filter(id=id)
            if len(name.strip())!=0:
                return Test.objects.filter(name=name)

class hgt(models.Model):
    type=models.CharField(max_length=10)
    yue=models.FloatField()
    liuru=models.FloatField()
    shangzhang=models.IntegerField()
    chiping=models.IntegerField()
    xiadie=models.IntegerField()
    createtime=models.DateTimeField()
    dapanzhangfu=models.FloatField()
    def insert(self,type=None,yue=None,liuru=None,shangzhang=None,chiping=None,xiadie=None,createtime=None,dapanzhangfu=None):
        hgt.objects.create(type=type,yue=yue,liuru=liuru,shangzhang=shangzhang,chiping=chiping,xiadie=xiadie,createtime=createtime,dapanzhangfu=dapanzhangfu)
