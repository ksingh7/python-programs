import subprocess

cmd = "ls -l /etc/resolv.conf"
out_call = subprocess.call(cmd.split())
out_check_call = subprocess.check_call(cmd.split())
out_check_output = subprocess.check_output(cmd.split())

print(out_check_output)

