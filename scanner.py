#!/usr/bin/python -O

import os
from subprocess import check_output
from utils import *

class FileScanner:

    """ Returns a structure of all files mathching the filter """

    def getChanged(self, root):
        try:
            os.chdir(root)
            changed_files = (check_output("git diff-tree --no-commit-id --name-only -r HEAD", shell=True)).split()
        except:
            raise

        return [os.path.abspath(p) for p in changed_files]

    def scan(self, root, ext):
        return check_output("""find %s -iname "*.%s""" % (root, ext), shell=True).split()
