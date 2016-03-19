#!/bin/python
import subprocess

def findCorruptJournal(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    p_status = p.wait()
    #print "return code", p_status
    if p_status >= 1:
    #print err
        error_string=err.split()
    for i in range(len(error_string)-1,0,-1):
        temp = error_string[i]
   if temp.find("system.journal") > -1:
#      print temp
      break
remove_journal_log = "rm -rf "+temp
#print remove_journal_log


p = subprocess.Popen(remove_journal_log, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
p = subprocess.Popen(['systemctl','restart',' systemd-journald.service'], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
p_status = p.wait()
out, err = p.communicate()
if p_status == 0:
  print "Journal logs cleaned"
else:
  print "There was some error while cleaning journal logs"
  print err

  
cmd = "journalctl --verify"
findCorruptJournal(cmd)