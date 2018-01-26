#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Git post-commit hook to remove private values """
""" TEST Version """

import sys, subprocess

from cmnds import run_cmnds


def main():

	cmnds = ['python3 ../py-hook.py "post" "test.files/group_vars" "../test.bak/group_vars"',
	 'python3 ../py-hook.py "post" "test.files/host_vars" "../test.bak/host_vars"']
	
	run_cmnds(cmnds)
	

if __name__ == "__main__":
	main()
