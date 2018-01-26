#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Python function to run commands in a list """
""" TEST Version """

import sys, subprocess

def run_cmnds(cmnds):
	
	for cmnd in cmnds:
	
		print("CMD: " + cmnd) 
		
		# Source: https://stackoverflow.com/questions/16198546/get-exit-code-and-stderr-from-subprocess-call
		try:
			output = subprocess.check_output(
			cmnd, stderr=subprocess.STDOUT, shell=True, timeout=30,
				universal_newlines=True)
		except subprocess.CalledProcessError as exc:
			print("ERROR: ", exc.returncode, exc.output)
			return exc.returncode
			sys.exit(1) # command failed to execute successfully
		else:
			print("OUTPUT: \n{}\n".format(output))
	
	#sys.exit(0) # return success (0) and exit
