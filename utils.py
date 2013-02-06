#!/usr/bin/python -O

import os

class Course:
	name = ""
	
	projects = {}

	def __init__(self, name):
		self.name = name


class Project:
	name = ""
	file_paths = []
	

	def __init__(self, name):
		self.name = name

	def getTempDir(self, temp_dir):
		"""temp_dir is the global tmp directory"""
		dir = os.path.join(temp_dir, self.name)
		
		if not os.path.exists(dir):
			os.makedirs(dir)
		
		return dir



