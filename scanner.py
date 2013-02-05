#!/usr/bin/python -O

import os
from utils import *

class FileScanner:

	""" Returns a structure of all files mathching the filter """

	filters = []
	
	def __init__(self, f):
		self.filters = f

	def scan(self, root):
		if not os.path.exists(root):
			raise Error
		
		courses = [Course(os.path.abspath(x)) 
				for x in os.listdir(root) 
				if os.path.isdir(x) and x[0] != "."]
		
		for course in courses:
			#Lets find all Projects
			course.projects = [Project(os.path.join(course.path,x))
                                   for x in os.listdir(course.path)
                                   if os.path.isdir(os.path.join(course.path, x))
					and x[0] != "."]

			for project in course.projects:
				#Recursively find all files that matches filters
				def find(p):
					files = [os.path.join(p,x) 
						for x in os.listdir(p)
						if x[0] != "."]
					
					for file in files:
						if os.path.isdir(file):
							find(file)
						elif os.path.isfile(file) and file[file.rfind(".") + 1:] in self.filters:
							project.file_paths.append(os.path.abspath(file))
				find(project.path)
		return courses
