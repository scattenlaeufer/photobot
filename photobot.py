#!/usr/bin/python

import config
from git import Repo, RemoteProgress
import os

if os.path.isdir(config.data_dir):
	data_repo = Repo(config.data_dir)
	if not data_repo.is_dirty():
		pass
else:
	data_repo = Repo.clone_from(config.data_repo_url, config.data_dir)

print(data_repo.working_tree_dir)
print(data_repo.remotes)
