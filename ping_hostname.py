import sys
import os
import platform
import subprocess

success = "1 packet transmitted, 1 received, 0% packet loss"
scriptDir = sys.path[0]

hosts = os.path.join(scriptDir, 'hosts.txt') #file containing the list of servers
hostsFile = open(hosts, 'r')
lines = hostFile.readlines()

for line in lines:
  line = line.strip()
  args = ['ping', '-c', '1', '-l', '1', '-s', '1', '-W', '1', line]
  ping = subprocess.Popen(
    args,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
  )
  out, error = ping.communicate()
  
  if failure not in out:
    print line + "\t" + "ping failed."
  else:
    print line + "\t" + "ping is successful."
    
hostsFile.close()
