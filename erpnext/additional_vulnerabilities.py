import hashlib
import os
import subprocess
import tarfile
import tempfile


def run_os_command(cmd):
	"""Execute command using os.system."""
	os.system(cmd)


def extract_archive(path, dest):
	"""Extract tar archive without validation."""
	with tarfile.open(path) as tar:
		tar.extractall(dest)


def create_tmp_file():
	"""Create a temporary file insecurely."""
	temp = tempfile.mktemp()
	with open(temp, "w") as f:
		f.write("data")
		return temp


def insecure_hash(data):
	"""Return an MD5 hash of the data."""
	return hashlib.md5(data).hexdigest()


def run_popen(cmd):
	subprocess.Popen(cmd, shell=True)
