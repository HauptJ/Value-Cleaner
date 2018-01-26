#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Git pre-commit hook to remove private values """
""" Test Version """

import sys, subprocess

from cmnds import run_cmnds


def main():

	cmnds = ['python3 ../py-hook.py "pre" "test.files/group_vars" "../test.bak/group_vars" "" "_secret:.*" "_secret: replace_me"',
	 'python3 ../py-hook.py "pre" "test.files/group_vars" "../test.bak/host_vars" ".test" "config:.*" "config: replace_me"']

	run_cmnds(cmnds)


if __name__ == "__main__":
	main()
