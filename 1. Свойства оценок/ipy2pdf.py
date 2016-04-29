#!/usr/bin/python

#      DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or 
# modified copies of this license document, and changing 
# it is allowed as long as the name is changed.
#
#         DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# 	TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND 
# 					MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

import os, sys
import shutil

ip_name = sys.argv[1]

assert ip_name[-6:] == '.ipynb', 'Wrong format. Only .ipynb supported'

name = ip_name[:len(ip_name)-5]  ## with '.' at the end

tex_name = ip_name[:len(ip_name)-5]+"tex"
tmp_name = "_"+tex_name

os.system("jupyter nbconvert {} --to latex".format(ip_name))

pttrn = "\documentclass"
ins = "    \usepackage[T2A]{fontenc}\n \
			\usepackage[utf8]{inputenc}\n \
			\usepackage[cp1251]{inputenc}\n \
			\usepackage[english,russian]{babel}\n"

with open(tex_name, "r") as f_old, \
	open(tmp_name, "w") as f_new:
	flag = 1
	for line in f_old:
	    f_new.write(line)
	    if flag and (pttrn in line):
	    	flag = 0
	        f_new.write(ins)

os.remove(tex_name)
os.rename(tmp_name,tex_name)

os.system("pdflatex -interaction=nonstopmode {} > \
			 /dev/null".format(tex_name))

shutil.rmtree(name[:-1]+"_files")
os.remove(name+"log")
os.remove(name+"tex")
os.remove(name+"aux")
os.remove(name+"out")
