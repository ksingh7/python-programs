import psutil , datetime, subprocess

def cpu_usage():
  cpu_usage = psutil.cpu_percent(interval=1)
  if cpu_usage <= 60:
      print "CPU utilization is OK"
  elif cpu_usage > 60 and cpu_usage <= 80:
      print "CPU utilization is WARNING"
  else:
      print "CPU utilization is CRITICAL"
  print "current CPU utilization % is : " + str(cpu_usage) + "\n"

def memory_usage():
  mem_usage = psutil.virtual_memory()
  if mem_usage <= 59:
      print "Memory utilization is OK"
  elif 60 < mem_usage > 79:
      print "Memory utilization is WARNING"
  elif mem_usage >= 100:
      print "Memory utilization is CRITICAL"
  print "current MEMORY utilization % is : " + str(mem_usage.percent) + "\n"

def swap_memory_usage():
  mem_usage = psutil.swap_memory()
  print "current SWAP MEMORY utilization % is : " + str(mem_usage.percent) + "\n"

def disk_usage():
  disk_usage = subprocess.Popen(["df","-h"], shell=False)
  print "current disk usage of the system is :"
  print disk_usage

def disk_io_counter():
    disk_io_counter = psutil.disk_io_counters()
    print "\ncurrent disk READ IOPS % is : " + str(disk_io_counter.read_count)
    print "current disk WRIE IOPS % is : " + str(disk_io_counter.write_count)
'''
def email_sender(input_message, email_to, client):

    to = email_to
    gmail_user = 'greengoblin064@gmail.com' ## email of sender account
    gmail_pwd = 'alohamora007' ## password of sender account
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: System Monitoring Report \n'
    input_message = input_message + client
    msg = header + input_message
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
'''

print "------------------------------------------------------------------"
d = datetime.datetime.now()
print "System Monitoring Report generate at : " + str(d)
print "------------------------------------------------------------------\n"
cpu_usage()
memory_usage()
swap_memory_usage()
disk_usage()
disk_io_counter()





