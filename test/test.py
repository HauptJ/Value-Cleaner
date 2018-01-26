#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Test script for Value-Cleaner """

import sys, subprocess, filecmp, os, cmnds

def get_common_files(dir_A, dir_B):
	
	# Determine the items that exist in both directories
	# Source: https://pymotw.com/3/filecmp/
	d1_contents = set(os.listdir(dir_A))
	d2_contents = set(os.listdir(dir_B))
	common = list(d1_contents & d2_contents)
	common_files = [
		f
		for f in common
		if os.path.isfile(os.path.join(dir_A, f))
	]

	print('Common files:', common_files)
	return common_files
	

def test_dirs(test_name, are_diff, dir_A, dir_B):
	
	common_files = get_common_files(dir_A, dir_B)
	
	match, mismatch, errors = filecmp.cmpfiles(dir_A, dir_B, common_files)
	
	print("Directory stats: ")
	print('Match       :', match)
	print('Mismatch    :', mismatch)
	print('Errors      :', errors)
	
	if len(mismatch) > 0:
		print("TEST: " + test_name + " files are not the same in directory " + dir_A + " and directory " + dir_B + "\n \t REPORT: \n")
		
		# generate report
		report = filecmp.dircmp(dir_A, dir_B)
		print(report.report_full_closure())
		
		if are_diff == True:
			print("TEST: " + test_name + " PASSED \n")
			return True
		
		elif are_diff == False:
			print("TEST: " + test_name + " FAILED \n")
			return False
		
		else:
			print("TEST: " + test_name + " ERROR \n")
			return False
		
	elif len(mismatch) == 0:
		print("TEST: " + test_name + " files are the same in directory " + dir_A + " and directory " + dir_B + "\n")
		
		if are_diff == False:
			print("TEST: " + test_name + " PASSED \n")
			return True
			
		elif are_diff == True:
			print("TEST: " + test_name + " FAILED \n")
			return False
			
		else:
			print("TEST: " + test_name + " ERROR \n")
			return False
			
	print("TEST: " + test_name + " ERROR with result: ")
	return False
		
		
def main():
	
	total_tests = 0
	passed_tests = 0
	
	# lists
	passed_list = []
	failed_list = []

	######## pre-commit: Key is present ########
	
	pre_cmnd_pres = ['python3 pre_commit_test_present.py']
	
	# Run pre-commit test like it is a git hook
	cmnds.run_cmnds(pre_cmnd_pres)
	
	name = "pre_commit_key_present"
	src = "test.files/group_vars"
	bak = "../test.bak/group_vars"
		
	# Compare cleaned source directory with backup directory.
	# If the key is present, they should not be the same.
	
	res = test_dirs(name, True, src, bak)
	if res == True:
		passed_tests += 1
		passed_list.append(name)
	else:
		failed_list.append(name)
	total_tests += 1
		
	
	##### pre-commit: Directory backup #####
	
	name = "pre_commit_directory_backup"
	orig = "test.orig/group_vars"
	bak = "../test.bak/group_vars"
		
	# Compare original directory with the backup directory
	# They should be the same
	
	res = test_dirs(name, False, orig, bak)
	if res == True:
		passed_tests += 1
		passed_list.append(name)
	else:
		failed_list.append(name)
	total_tests += 1
	
	######## Post commit ########
	
	post_cmnd = ['python3 post_commit_test.py']
	
	# Run post-commit test like it is a git hook
	cmnds.run_cmnds(post_cmnd)
	
	##### post-commit: Restore backup #####
	
	name = "post_commit_directory_restore"
	orig = "test.orig/group_vars"
	src = "test.files/group_vars"
	
	# Compare original directory with the restored backup directory
	# They should be the same
	
	res = test_dirs(name, False, orig, src)
	if res == True:
		passed_tests += 1
		passed_list.append(name)
	else:
		failed_list.append(name)
	total_tests += 1
	
	######## pre-commit: Key is not present ########
	
	pre_cmnd_abs = ['python3 pre_commit_test_absent.py']
	
	# Run pre-commit test like it is a git hook
	cmnds.run_cmnds(pre_cmnd_abs)
	
	name = "pre_commit_key_absent"
	src = "test.files/group_vars"
	bak = "../test.bak/group_vars"
		
	# Compare cleaned source directory with backup directory.
	# If the key is absent, they should be the same.
		
	res = test_dirs(name, False, src, bak)
	if res == True:
		passed_tests += 1
		passed_list.append(name)
	else:
		failed_list.append(name)
	total_tests += 1
	
	##### pre-commit: Directory backup #####
	
	name = "pre_commit_directory_backup"
	orig = "test.orig/group_vars"
	bak = "../test.bak/group_vars"
		
	# Compare original directory with the backup directory
	# They should be the same
	
	res = test_dirs(name, False, orig, bak)
	if res == True:
		passed_tests += 1
		passed_list.append(name)
	else:
		failed_list.append(name)
	total_tests += 1
	
	######## Post commit ########
	
	post_cmnd = ['python3 post_commit_test.py']
	
	# Run post-commit test like it is a git hook
	cmnds.run_cmnds(post_cmnd)
	
	##### post-commit: Restore backup #####
	
	name = "post_commit_directory_restore"
	orig = "test.orig/group_vars"
	src = "test.files/group_vars"
	
	# Compare original directory with the restored backup directory
	# They should be the same
	
	res = test_dirs(name, False, orig, src)
	if res == True:
		passed_tests += 1
		passed_list.append(name)
	else:
		failed_list.append(name)
	total_tests += 1
	
	######## Summary ########
	
	failed_tests = total_tests - passed_tests
	
	print("Summary: ")
	
	print("Tests passed: " + str(passed_tests) + " Tests failed: " + str(failed_tests) + "\n")
		
	if passed_tests == total_tests:
		print("All tests were successful \n")
		print("Passed tests: ")	
		print(passed_list)
		sys.exit(0) # All tests passed
	else:
		print("Some tests failed \n")
		print("Failed tests: ")
		print(failed_list)
		print("Passed tests: ")	
		print(passed_list)
		sys.exit(1) # Not every test passed
	

if __name__ == "__main__":
	main()
