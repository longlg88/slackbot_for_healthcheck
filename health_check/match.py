import os
import sys
import re

def get_live_host_env1(host_env1_id):
	f=open('./host_env1_info','r')
	lines=f.readlines()
	host_name=[]
	host_id=[]
	on_msg=[]
	off_msg=[]
	
	for s in lines:
		host_name.append(s.split('\t')[0])
		host_id.append(int(s.split('\t')[1].replace('\n','')))
	s=set(host_env1_id)
	hostname_on=[x for x in host_id if x in s]
	hostname_off=[x for x in host_id if x not in s]
	print(hostname_off)
	for x in range(0, len(hostname_on)):
		on_msg.append(host_name[x]+'    ON')
	for y in range(len(hostname_on), len(hostname_off)):
		off_msg.append(host_name[y]+'    OFF')
	return_msg = "\n".join(on_msg) + '\n'+ "\n".join(off_msg)
	#print(return_msg)
	return return_msg


	
#if __name__=="__main__":
#	host_env1_id=[10000026,10000027]
#	get_live_host_env1(host_env1_id)
