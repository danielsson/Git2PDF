#!/usr/bin/python -O

import os
from subprocess import check_output
from utils import *

class FileScanner:

    """ Returns a structure of all files mathching the filter """

    filters = []
    
    def __init__(self, f):
        self.filters = f
    
    def scan(self, root, levels = 0):
        try:
            os.chdir(root)
            changed_files = (check_output("git diff-tree --no-commit-id --name-only -r HEAD", shell=True)).split()
        except:
            raise

        courses = {}
	print changed_files
        for f in changed_files:
            course, project, path = self.splitParts(root,f)
            if False in (course, project, path):
                continue

            if path[path.rfind(".") + 1:] not in self.filters:
                continue # Filter out 

            if(course not in courses):
                courses[course] = Course(course)

            if(project not in courses[course].projects):
                courses[course].projects[project] = Project(project)

            courses[course].projects[project].file_paths.append(path)

        return courses

    #Divide the specified path into course, project, abs-path
    def splitParts(self, root, path):
        parts = path.split('/', 2)
        if len(parts) != 3: return False, False, False
        parts[2] = os.path.abspath(os.path.join(root, parts[0], parts[1], parts[2]))
        return parts[0], parts[1], parts[2]


    def scan_old(self, root):
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
