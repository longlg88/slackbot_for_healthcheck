import os
import json
import sys
import requests
import time

def get_hostid_env1():
	res_host_ids_env1=requests.get("http://175.195.163.24:8080/SysManager/sysmanager/AgentList?action=Service")
	#res_host_ids_env2=requests.get("http://175.195.163.29:8080/SysManager/sysmanager/AgentList?action=Service")

	if(res_host_ids_env1.status_code == 500 ):
		print("error env1 \n", res_host_ids_env1.json())
		sys.exit()
	#elif(res_host_ids_env2.status_code == 500):
	#	print("error env2 \n", res_host_ids_env2.json())
	#	sys.exit()
	#elif(res_host_ids_env1.status_code == 500 and res_host_ids_env2.status_code == 500):
	#	print("error env1 & env2 \n", res_host_ids_env1.json(), res_host_ids_env2.json())
	#	sys.exit()
	else:
		DIR_JSON='./json/hostid'
		if not os.path.exists(DIR_JSON):
			os.makedirs(DIR_JSON)
		with open(DIR_JSON+"/host_env1_ids.json",'w') as host_make_file:
			#json.dump(res_host_ids_env1.json(), host_make_file, ensure_ascii=False, indent='\t', sort_keys=True)
			json.dump(res_host_ids_env1.json(), host_make_file, encoding='utf-8')
			#print(res_host_ids_env1.json())
		with open(DIR_JSON+"/host_env1_ids.json") as host_data_file:
			host_env1 = json.load(host_data_file)

		return host_env1
		#host_env1_len=len(host_env1['dto']['result'])
		#print('host env1 length = ',host_env1_len)
		#for x in range(0, host_env1_len):
		#	print('host env1 results = ',type(host_env1['dto']['result'][x]))

#if __name__=="__main__":
#	get_hostid_env1()
