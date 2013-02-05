#!/usr/bin/python -O

import os

class Course:
	name = ""
	path = ""
	
	projects = []

	def __init__(self, path):
		self.path = path
		self.name = os.path.split(path)[1]


class Project:
	name = ""
	path = ""
	file_paths = []
	
	output_path = ""
	

	def __init__(self, path):
		self.path = path
		self.name = os.path.split(path)[1]

	def getTempDir(self, temp_dir):
		"""temp_dir is the global tmp directory"""
		dir = "%s/%s" % (temp_dir, self.name)
		
		if not os.path.exists(dir):
			os.makedirs(dir)
		
		return dir



