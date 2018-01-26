#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Python script to remove sensitive variable info from files during git commit. """

import sys, shutil, errno, re, os, fileinput

# Source: https://stackoverflow.com/questions/1994488/copy-file-or-directories-recursively-in-python
def copy_dir(src, bak):
	
	try:
		shutil.copytree(src, bak)
	except OSError as exc:
		if exc.errno == errno.ENOTDIR:
			print("ERROR: The source directory specified: " + src + " is not a directory but a file. \n")
			sys.exit(3)
		else: 
			raise
			sys.exit(4) # copy_dir() failed with shutil.copytree()
        

def delete_dir(bak):
	
	try:
		shutil.rmtree(bak)
	except OSError as exc:
		if exc.errno == errno.ENOTDIR:
			print("ERROR: The backup directory specified: " + bak + " is not a directory but a file. \n")
			sys.exit(5)
		else:
			raise
			sys.exit(6) # delete_dir() failed with shutil.rmtree()
	
   
# Source: https://docs.python.org/3/library/fileinput.html
def proc_file(file_path, key, repl):
	
	with fileinput.input(files=(file_path), inplace=True) as f:
		for line in f:
			sys.stdout.write(re.sub(key, repl, line))
        
        
# Source: https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
def walk_dir(src, exten, key, repl):
	
	for dirpath, dirnames, files in os.walk(src):
		for name in files:
			if name.lower().endswith(exten):
				proc_file(os.path.join(dirpath, name), key, repl) # replace line with private info with one with clean info


def check_dir(bak):
	
	# make sure source directory is not in git repo
	if bak.find("..") == -1:
		print("ERROR: Destination directory: " + bak + " is in the git repository. \n")
		sys.exit(2) # return destination directory error (2) and exit
		
				
def pre_commit(src, bak, exten, key, repl):
	
	check_dir(bak)
	
	# copy original files to backup directory
	print("Making copy of directory: " + src + " in: " + bak + " \n")
	copy_dir(src, bak)

	# clean files
	print("Cleaning files in: " + src + " \n")
	walk_dir(src, exten, key, repl)
	sys.exit(0) # return success (0) and exit

	
def post_commit(src, bak):
	
	check_dir(bak)
	
	# delete cleaned directory
	print("Deleting cleaned directory: " + src + " \n")
	delete_dir(src)

	# restore original files
	print("Restoring directory: " + src + " from backup: " + bak + " \n")
	copy_dir(bak, src)
	
	# delete backup directory
	print("Deleting backup directory: " + bak + " \n")
	delete_dir(bak)
	sys.exit(0) # return success (0) and exit
	
		
def main():
		
	# pre-commit
	if len(sys.argv) == 7 and sys.argv[1].lower() == "pre":
		
		stage = sys.argv[1] # pre or post commmit 
		src = sys.argv[2] # source directory
		bak = sys.argv[3] # backup directory
		exten = sys.argv[4] # file extension to search for
		key = sys.argv[5] # key / substring to look for in line
		repl = sys.argv[6] # string to replace key in line
		
		print("values provided: " + "stage: " + stage + " source: " + src + " backup: " + bak + " extension: " + exten + " key: " + key + " replacement: " + repl + "\n")

		pre_commit(src, bak, exten, key, repl)
	
	# post-commit
	elif len(sys.argv) == 4 and sys.argv[1].lower() == "post":
		
		stage = sys.argv[1] # pre or post commmit 
		src = sys.argv[2] # source directory
		bak = sys.argv[3] # backup directory
		
		print("values provided: " + "stage: " + stage + " source: " + src + " backup: " + bak + "\n")
		
		post_commit(src, bak)

	# invalid arguments
	else:
		print("ERROR: Invalid Usage \n values provided: ")
		print(sys.argv[1:])
		print("Usage : " + sys.argv[0]  + ' ["pre" or "post"] "source directory" "backup directory" "file extension" "value to replace" "replacement value"')
		sys.exit(1) # return argument error (3) and exit
		
				
if __name__ == "__main__":
    main()
