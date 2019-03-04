from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
import os
import logging
import subprocess

logging.basicConfig()
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

def Watch_func(event):
	f = open("check","r")
	a = int(f.read())
	f.close()
	child = zk.get_children("/")
	child.remove('zookeeper')
	if(val[1:] == sorted(child)[0] and a != len(child)):
		print "MASTER"
		subprocess.call(['gnome-terminal -e ./single.sh'],shell = True)
	print "New process is called by " + sorted(child)[0] + " since it is MASTER" 
	time.sleep(20)


val = zk.create("/",b"kiran",ephemeral=True,sequence=True)
child = zk.get_children("/")
child.remove('zookeeper')
print("There are %s children with names %s" % ((len(child)), child ))
f = open("check","w")
f.write(str(len(child)))
f.close()
c = 0
while(1):
	time.sleep(4)
	child = zk.get_children("/",watch = Watch_func)
	child.remove('zookeeper')
	if(c%3 == 0):
		os.system('clear')
		if(val[1:] == sorted(child)[0]):
			print "I AM MASTER " + sorted(child)[0]
		else:
			print "I AM AGENT " + val[1:]
			print "My MASTER is " + sorted(child)[0]
		print " "
		print "%s children %s" % (len(child), child)
	c = c + 1
