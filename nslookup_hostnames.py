import sys
import os
import platform
import subprocess

failure = "** server can't find"
scriptDir = sys.path[0]

hosts = os.path.join(scriptDir, 'hosts.txt') #file containing the list of servers
hostsFile = open(hosts, 'r')
lines = hostFile.readlines()

for line in lines:
  line = line.strip()
  args = ['nslookup', line]
  ping = subprocess.Popen(
    args,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
  )
  out, error = ping.communicate()
  
  if failure not in out:
    print line + "\t" + "nslookup successful."
  else:
    print line + "\t" + "nslookup not successful."
    
hostsFile.close()
