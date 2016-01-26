#!/usr/bin/python

import subprocess
import sys

def Sendmail(message):
    SENDMAIL = "/usr/sbin/sendmail"
    TO = "unxi-admins@example.com"
    FROM = "ssh-bot@example.com"
    SUBJECT = "SSH output report"

    import  os
    p = os.popen("%s -t -i" % SENDMAIL, "w")
    p.write(message)
    status = p.close()
    if status:
      print "Sendmail exit status", status

fname = "/Users/ksingh/temp/host_list"
user_name = "cloud-user"
command = "date"

with open(fname) as f:
  host = f.read().splitlines()

for i in host:
  ssh_host = user_name + "@" + i
  ssh = subprocess.Popen(["ssh", "%s" % ssh_host, command],
			 shell=False,
			 stdout=subprocess.PIPE,
			 stderr=subprocess.PIPE)
  result = ssh.stdout.readlines()
  if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
  else:
    print result[0]
    Sendmail(result[0])