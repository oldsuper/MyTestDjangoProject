__author__ = 'Administrator'

from django.http import HttpResponse
from mymodel.models import Test
from mymodel.models import hgt
from django.shortcuts import *
import httplib2
import urllib
import time

def testdb(request):
    list = Test.objects.all()
    response = ""
    # print "type",type(list[0].name.encode('utf8'))
    for i in list:
        response = response + str(i.id) + i.name.encode('utf8')

    return HttpResponse(response)
def insert(request):
    return render_to_response('insertGet.html')
def do(request):
    msg="pass"
    request.encoding='utf-8'
    t=Test()
    print type(request.GET['id'].encode('utf8'))
    t.insert(int(request.GET['id'].encode('utf8')),request.GET['name'].encode('utf8'))
    return HttpResponse(msg)

def select(request):
    return render_to_response('select.html')
def select_res(request):
    id=request.GET['id'].encode('utf8')
    name=request.GET['name'].encode('utf8')
    print "id:",id,"name:",name,"end",len(name.strip())
    t=Test()
    resp=t.get(id,name)
    # print resp.__len__()
    if len(resp)==0:
        return HttpResponse(msg)
    for item in resp:
        msg = msg+str(item.id)+'\t'+item.name
    return HttpResponse(msg)

def hgt_insert(request):
    return render_to_response('hgt.html')
def hgt(request):
    msg="pass"
    h=hgt()
    hgturl='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=DPAB&sty=AHTZJL&js=({data:[(x)],time:%22(ut)%22})&cb=callback0412899351445958&callback=callback0412899351445958&_=1453111333550'
    http=httplib2.Http()
    r,c=http.request(hgturl)
    d=eval(c[c.find('(')+1:-1].replace('data','"data"').replace('time','"time"'))
    for item in d['data']:
        type=item[0]
        yue=item[1]
        liuru=item[2]
        shangzhang=item[3]
        chiping=item[4]
        xiadie=item[5]
        createtime=time.strftime("%Y-%m-%d ", time.localtime())+d['time']
        d.insert(type,)


    return HttpResponse(msg)