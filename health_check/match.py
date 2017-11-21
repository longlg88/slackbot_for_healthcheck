import os
import sys
import re

def get_live_host_env(num, host_env1_id):
	if num == 1:
		f=open('./host_env1_info','r')
	elif num == 2:
		f=open('./host_env2_info','r')
	else:
		print("wrong environment here")
		sys.exit()

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
	print(host_id)
	print(hostname_on)
	print(hostname_off)

	num=0
	num2=0
	
	for x in range(0, len(host_id)):
		if host_id[x] == hostname_on[num]:
			on_msg.append(host_name[x]+'    ON')
			num=num+1
		if num == len(hostname_on):
			break

	for y in range(0, len(host_id)):
		if host_id[y] == hostname_off[num2]:
			off_msg.append(host_name[y]+'    OFF')
			num2=num2+1
		if num2 == len(hostname_off):
			break

	return_msg = "\n".join(on_msg) + '\n'+ "\n".join(off_msg)
	#print(return_msg)
	return return_msg

#if __name__=="__main__":
#	host_env1_id=[10000026,10000027]
#	get_live_host_env1(host_env1_id)
