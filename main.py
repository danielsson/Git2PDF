#!/usr/bin/python -O

from subprocess import call, check_output
import os
import utils
from scanner import *
from pdfmaker import *


working_dir = "/tmp/autopdf"
git_dir     = os.path.abspath("/home/matt/autopdf/git") #Must exist, and be a git rep.

if not os.path.exists(working_dir):
    os.makedirs(working_dir)

def fail(msg):
    with open("log.txt", "a") as log:
        log.write(msg)
    raise



#Update GIT
try:
    os.chdir(git_dir)
    call("git pull", shell=True) and fail("oops")
except:
    fail("git update failed")


#Get all courses
print git_dir

scanner = FileScanner()
pdfmaker = PDFMaker()

courses = utils.makeStructure(git_dir, ("txt", "go"))
changes = scanner.getChanged(git_dir)

touched_projects = []

for course in courses:
    for project in course.projects:
        #Skip if no changes
        if True or any(i in project.file_paths for i in changes): #Disable smarts for now
            if len(project.file_paths) == 0: continue
            pdfpath = pdfmaker.make(project.name, project.file_paths, project.getTempDir(working_dir))
            
            #move the generated pdf to the project
            shutil.copy(pdfpath, project.path)
            
            touched_projects.append(project.name)

#lets save our work
os.chdir(git_dir)
git_message = "Git2PDF changes: " + " ".join(touched_projects)
if len(touched_projects):
	call("""git add . && git commit -m "%s" """ % git_message, shell=True) and fail("could not commit")
	call("git push", shell=True)


#cleanup
shutil.rmtree(working_dir)

