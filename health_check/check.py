# -*- coding: utf-8 -*-

import os
import time
from slackclient import SlackClient
import parse
import match

######
# this program is slack server so it runs background(if it isn't disturbing)
# 'handle_command' function is used for handling results in slack app
######
def handle_command(channel):
	host_env1=parse.get_hostid_env1()
	host_env1_len=len(host_env1['dto']['result'])
	host_env1_id=[]
	for x in range(0, host_env1_len):
		host_env1_id.append(host_env1['dto']['result'][x])

	env1_res=match.get_live_host_env1(host_env1_id)
	response='Sysmanager agent live check \n'+ 'Release Environment(env1)\n'+env1_res
	slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
	output_list=slack_rtm_output
	if output_list and len(output_list) > 0:
		for output in output_list:
			if output and 'text' in output and AT_BOT in output['text']:
				return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
	#for output in output_list:
	#	if 'channel' in output:
	#		return None, output['channel']
	return None, None

BOT_NAME='sysagent_healthcheck'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

BOT_ID=os.environ.get("BOT_ID")
AT_BOT = "<@"+BOT_ID+">"

if __name__=="__main__":
################################# BOT_ID CALL code
#	api_call = slack_client.api_call("users.list")
#	if api_call.get('ok'):
#		users=api_call.get('members')
#		for user in users:
#			if 'name' in user and user.get('name') == BOT_NAME:
#				print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
#################################
#################################

	if slack_client.rtm_connect():
		######################### waiting for client sending message 1s cycle
		print(slack_client.rtm_read())
		READ_WEBSOCKET_DELAY=1
		print("start bot!! BOT NAME is " + BOT_NAME)
		while True:
			command,  channel = parse_slack_output(slack_client.rtm_read())
			print command, channel
			if channel:
				handle_command(channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("could not find bot user with the name " + BOT_NAME)
