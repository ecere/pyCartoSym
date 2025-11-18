#!/usr/bin/env python
import subprocess
import sys
import os

def main():
   binary_path = os.path.join(os.path.dirname(__file__), 'cs-canif')
   result = subprocess.run(
      [binary_path] + sys.argv[1:],
      stdin=sys.stdin,
      stdout=sys.stdout,
      stderr=sys.stderr)
   sys.exit(result.returncode)
