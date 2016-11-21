#!/usr/bin/python

import config
from git import Repo, RemoteProgress
from fivehundredpx.auth import OAuthHandler
import os
import datetime
import oauth2

class MyProgressPrinter(RemoteProgress):
	def update(self, op_code, cur_count, max_count=None, message=''):
		print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")

if os.path.isdir(config.data_dir):
	data_repo = Repo(config.data_dir)
	if not data_repo.is_dirty():
		remote = data_repo.remote()
		for fetch_info in remote.pull():
			print("Updated %s to %s" % (fetch_info.ref, fetch_info.commit))
else:
	data_repo = Repo.clone_from(config.data_repo_url, config.data_dir)

handler_500px = OAuthHandler(config.consumer_key, config.consumer_secret)
#help(handler_500px)
#token = handler_500px.get_request_token()

consumer = oauth2.Consumer(config.consumer_key, config.consumer_secret)
client = oauth2.Client(consumer)
resp, content = client.request('https://api.500px.com/v1/oauth/request_token', 'GET')

print(resp)
print(content)


# data_repo.index.add(['testout'])
# data_repo.index.commit('testcommit from ' + str(time))
# data_repo.remote().push()
