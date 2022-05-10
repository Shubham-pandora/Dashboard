def UrlReturn(service_name,instance_ip):
    return("http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=" + instance_ip + "&servicedescription=" + service_name)
           
           
service_name_Admin5 = 'Admin5'
Admin5_instance_ip = ['10.30.48.153','10.30.48.154','10.30.48.192']
Admin5153 = UrlReturn(service_name_Admin5, Admin5_instance_ip[0])
print(Admin5153)
