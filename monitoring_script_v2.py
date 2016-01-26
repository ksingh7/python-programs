import psutil , datetime, subprocess

def cpu_usage():
  cpu_usage = psutil.cpu_percent(interval=1)
  return "current CPU utilization % is : " + str(cpu_usage) + "\n"

def memory_usage():
  mem_usage = psutil.virtual_memory()
  return "current MEMORY utilization % is : " + str(mem_usage.percent) + "\n"

def swap_memory_usage():
  mem_usage = psutil.swap_memory()
  return "current SWAP MEMORY utilization % is : " + str(mem_usage.percent) + "\n"

def disk_usage():
  disk_usage = subprocess.Popen(["df","-h"], shell=False)
  return "current disk usage of the system is :" + str(disk_usage) + "\n"

def disk_io_counter():
  disk_io_counter = psutil.disk_io_counters()
  return 'current disk READ IOPS is %s and WRITE IOPS is %s : \n' % (str(disk_io_counter.read_count), str(disk_io_counter.write_count))

def email_sender(message, email_from, email_to):

    import smtplib

    gmail_user = email_from
    gmail_pwd = 'alohamora007'
    email_to = email_to

    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(gmail_user, gmail_pwd)

    header = 'To:' + email_to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: System Monitoring Report \n'
    input_message = message
    msg = header + input_message
    smtpserver.sendmail(gmail_user, email_to, message)
    smtpserver.close()
    smtpserver.quit()
    print "message sent"

message = "------------------------------------------------------------------\n"
d = datetime.datetime.now()
message = message + "System Monitoring Report generate at : " + str(d)
message = message + "\n------------------------------------------------------------------\n"


cpu_usage = cpu_usage()
message = message + str(cpu_usage)

memory_usage = memory_usage()
message = message + str(memory_usage)

swap_usage = swap_memory_usage()
message = message + str(swap_usage)

disk_IOPS = disk_io_counter()
message = message + str(disk_IOPS)

disk_usage = disk_usage()
message = message + str(disk_usage)

#print message
email_sender(message,'greengoblin064@gmail.com','karan.singh731987@gmail.com')

