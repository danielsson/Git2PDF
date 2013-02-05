#!/usr/bin/python -O

from utils import *
import os, shutil
from subprocess import call


class PDFMaker:
	
	def make(self, name, paths, tmpdir):
		"""Makes a pdf out of the files in the list paths"""
		
		
		#PS stage
		div = " "
		src_list = div.join(paths)
		
		ps_target = "%s/%s.ps" % (tmpdir, name)
	
		call("""a2ps %s -2 -C -T 4 --footer="AutoGit2PDF by Mattias Danielsson" --toc -g -o %s""" % (src_list, ps_target), shell=True)
		
		#make pdf
		pdf_target = "%s/%s.pdf" % (tmpdir, name)
		
		call("ps2pdf %s %s" % (ps_target, pdf_target), shell=True)
		
		#remove ps
		os.unlink(ps_target)

		return pdf_target
		 
		


