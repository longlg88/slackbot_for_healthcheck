import os
import json
import sys
import requests
import time

def get_hostid_env(num):
	DIR_JSON='./json/hostid'
	## get host id / env1
	if num == 1:
		res_host_ids_env1=requests.get("http://175.195.163.24:8080/SysManager/sysmanager/AgentList?action=Service")
		## exception
		if(res_host_ids_env1.status_code == 500 ):
			print("error env1 \n", res_host_ids_env1.json())
			sys.exit()
		else:
			if not os.path.exists(DIR_JSON):
				os.makedirs(DIR_JSON)
			with open(DIR_JSON+"/host_env1_ids.json",'w') as host_make_file:
				json.dump(res_host_ids_env1.json(), host_make_file, encoding='utf-8')
			with open(DIR_JSON+"/host_env1_ids.json") as host_data_file:
				host_env1 = json.load(host_data_file)

		return host_env1

	## get host id / env2
	elif num == 2:
		res_host_ids_env2=requests.get("http://175.195.163.29:8080/SysManager/sysmanager/AgentList?action=Service")
		## exception
		if(res_host_ids_env2.status_code == 500):
			print("error env2 \n", res_host_ids_env2.json())
			sys.exit()
		else:
			if not os.path.exists(DIR_JSON):
				os.makedirs(DIR_JSON)
			with open(DIR_JSON+'/host_env2_ids.json','w') as host_make_file:
				json.dump(res_host_ids_env2.json(), host_make_file, encoding='utf-8')
			with open(DIR_JSON+'/host_env2_ids.json') as host_data_file:
				host_env2 = json.load(host_data_file)
		return host_env2

	else:
		print("wrong environment here")
		sys.exit()

#if __name__=="__main__":
#	get_hostid_env1()
