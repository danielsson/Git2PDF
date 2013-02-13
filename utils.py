#!/usr/bin/python -O

import os
from scanner import FileScanner

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

def makeStructure(root, exts):
	scanner = FileScanner()

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
        	for ext in exts:
        		project.file_paths = project.file_paths + scanner.scan(project.path, ext)

    return courses