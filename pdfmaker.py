#!/usr/bin/python -O

from utils import *
import os, shutil
from subprocess import call


class PDFMaker:
    
    def make(self, name, paths, fdir):
        """Makes a pdf out of the files in the list paths
           name     The name of the file to generate
           paths    An array of paths to the files to compound
           dir      The dir to place the result. Will be used as tmp-dir for intermediary files

           Returns  The path to the generated file
        """
        
        
        #PS stage
        src_list = " ".join(paths)
        
        ps_target = "%s/%s.ps" % (fdir, name)
    
        print """a2ps %s -2 -C -T 4 --footer="github.com/mattenrone/Git2PDF" --toc -g -o %s""" % (src_list, ps_target)
        call("""a2ps %s -2 -C -T 4 --footer="github.com/mattenrone/Git2PDF" --toc -g -o %s""" % (src_list, ps_target), shell=True)
        
        #make pdf
        pdf_target = "%s/%s.pdf" % (fdir, name)
        
        call("ps2pdf %s %s" % (ps_target, pdf_target), shell=True)
        
        #remove ps
        os.unlink(ps_target)

        return pdf_target
         
        


