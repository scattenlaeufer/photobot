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
		for fetch_info in remote.pull(progress=MyProgressPrinter()):
			print("Updated %s to %s" % (fetch_info.ref, fetch_info.commit))
else:
	data_repo = Repo.clone_from(config.data_repo_url, config.data_dir, progress=MyProgressPrinter())

data_file = None
with open(os.path.join(config.data_dir, 'test'), 'r') as test_file:
	data_file = test_file.read()

data_list = data_file.split('\n')

time = datetime.datetime.now()
testout_path = os.path.join(data_repo.working_tree_dir, 'testout')

out_file = None
if os.path.isfile(testout_path):
	with open(testout_path, 'r') as testout_file:
		out_file = testout_file.read()
else:
	out_file = ''

out_list = out_file.split('\n')
out_list.append(data_list[-2])
out_file = '\n'.join(out_list)

with open(testout_path, 'w') as testout_file:
	testout_file.write(out_file)

print(data_repo.working_tree_dir)
data_repo.index.add(['testout'])
data_repo.index.commit('testcommit from ' + str(time))
data_repo.remote().push()


