import os
import pickle
import subprocess

import yaml


def run_command(user_cmd):
	# A vulnerability: using shell=True with unsanitized input
	subprocess.run(user_cmd, shell=True)


def eval_user_input(data):
	# Another vulnerability: eval on untrusted input
	eval(data)


def load_yaml(data):
	# YAML load without Loader: potential code execution
	return yaml.load(data)


def load_pickle(data):
	# Untrusted pickle deserialization
	return pickle.loads(data)
