#!/usr/bin/python -O

import os
import threading

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
		dir = os.path.join(temp_dir, self.name)
		
		if not os.path.exists(dir):
			os.makedirs(dir)
		
		return dir

class AsyncPdfMake(threading.Thread):
	name = ""
	paths = []
	tdir = ""

	def __init__(self, pdfmaker, name, paths, tdir):
		self.pdfmaker = pdfmaker
		self.name = name
		self.paths = paths
		self.tdir = tdir

	def run(self):
		self.pdfmaker.make(self.name, self.paths, self.tdir)


