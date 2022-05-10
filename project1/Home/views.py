from cgitb import html
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import json

# Create your views here.
def index(request):
    context = {
        'build':"build-Number",
        'ip':"IP"
    }
    # return HttpResponse("this is message")
    return render(request,'index.html',context)

def output(request):
   msg1=request.GET.get('buildno')
   msg2=request.GET.get('ipaddress')
   print(msg1,msg2)
   context = {
       'msg1':msg1,
       'msg2':msg2
   }        
   return render(request, 'output.html',context)

def about(request):
    context = {
        'build':"build-Number",
        'ip':"10.30.48.163"
    }
    return render(request,'about.html',context)

def services(request):
   build1=request.GET.get('buildno')
   build2=request.GET.get('ipaddress')
   print(build1,build2)
   return render(request, 'services.html',{'build1':build1,'build2':build2})

def pbx(request):    
    freeswitch161 = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=beta-161&servicedescription=Freeswitch'  
    result_freeswitch = webnagios(freeswitch161)
    print(result_freeswitch)
    return render(request, 'pbx.html',{'freeswitch161':result_freeswitch})

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('name')            
        Email = request.POST.get('email')
        contact = Contact(name=Name,email=Email,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')

def web(request):   
    # streams178 = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.178&servicedescription=Streams'
    service_name_Streams = 'Streams'
    streams_instance_ip = ['10.30.48.178','10.30.48.183','10.30.48.185']
    streams178 = UrlReturn(service_name_Streams, streams_instance_ip[0])
    result_streams178 = webnagios(streams178)
    
    streams183 = UrlReturn(service_name_Streams, streams_instance_ip[1])
    result_streams183 = webnagios(streams183)

    streams185 = UrlReturn(service_name_Streams, streams_instance_ip[2])
    result_streams185 = webnagios(streams185)
    print("-----------------------inside webfunction")
    print("178:" + result_streams178 + ",183:" + result_streams183,"185:" + result_streams185) 
    
    service_name_Admin5 = 'Admin5'
    Admin5_instance_ip = ['10.30.48.153','10.30.48.154','10.30.48.192']
    Admin5153 = UrlReturn(service_name_Admin5, Admin5_instance_ip[0])
    result_Admin5153 = webnagios(Admin5153)
    
    Admin5154 = UrlReturn(service_name_Admin5, Admin5_instance_ip[1])
    result_Admin5154 = webnagios(Admin5154)

    Admin5192 = UrlReturn(service_name_Admin5, Admin5_instance_ip[2])
    result_Admin5192 = webnagios(Admin5192)
    print(result_Admin5192)
    print("-----------------------inside webfunction")   
    # print("153:" + result_Admin5153 + ",154:" + result_Admin5154,"192:" + result_Admin5192)
    
    context = {
        'result_streams178':result_streams178,
        'result_streams183':result_streams183,      
        'result_streams185':result_streams185,      
        'result_Admin5153':result_Admin5153,      
        'result_Admin5154':result_Admin5154,      
        # 'result_Admin5192':result_Admin5192,      
    }     
    return render(request, 'web.html',context)
    # return render(request, 'web.html',{'result_streams178':result_streams178,'result_streams183':result_streams183,'result_streams185':result_streams185})

# ------------------------- shubham --------------------------------------------------------------------------------------------------------------------
def webnagios(passing_url):    
    request_url = passing_url
    # request_url = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.183&servicedescription=Streams'
    username = 'nagiosadmin'
    password = 'nagios@beta'
    session = requests.Session()
    request = session.get(request_url, auth=HTTPBasicAuth(username,password), verify=False) 
    data_json = json.loads(request.text)   
    print("----------------------------")
    print(data_json['data']['service']['plugin_output'])
        
    string = data_json['data']['service']['plugin_output']
    sub_str ="OK" 
    sub_str1 ="ok" 
   
    if (string.find(sub_str) != -1) or (string.find(sub_str1) != -1):
        print("Yes")
        flag = "Running"
        return flag
    else:
        print("No")
        flag = "Not Running" 
        return flag      
 
                
def UrlReturn(service_name,instance_ip):
    return("http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=" + instance_ip + "&servicedescription=" + service_name)
      
   
  

    
    
    
    
