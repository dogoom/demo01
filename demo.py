#!/usr/bin/python

import subprocess

def git_init():
    cmd = subprocess.call("git init", shell=True)
    return cmd
if __name__ == "__main__":
    git_init()
