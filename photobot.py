#!/usr/bin/python

import config
from git import Repo, RemoteProgress
import os
import datetime

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


# data_repo.index.add(['testout'])
# data_repo.index.commit('testcommit from ' + str(time))
# data_repo.remote().push()
