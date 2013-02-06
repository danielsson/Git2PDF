#!/usr/bin/python -O

import os
from subprocess import check_output
from utils import *

class FileScanner:

    """ Returns a structure of all files mathching the filter """

    filters = []
    
    def __init__(self, f):
        self.filters = f

    def getChanged(self, root):
        try:
            os.chdir(root)
            changed_files = (check_output("git diff-tree --no-commit-id --name-only -r HEAD", shell=True)).split()
        except:
            raise

        return [os.path.abspath(p) for p in changed_files]


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
                    
                    for file_ in files:
                        if os.path.isdir(file_):
                            find(file_)
                        elif os.path.isfile(file_) and file_[file_.rfind(".") + 1:] in self.filters:
                            abs_file_path = os.path.abspath(file_)

                            project.file_paths.append(abs_file_path)
                find(project.path)
        return courses
