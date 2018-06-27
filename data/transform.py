#!/usr/bin/env python3
#
# Usage:
#
#  $ transform.py < US.txt > US-fixed.txt
#  $ transform.py < CA.txt > CA-fixed.txt


import fileinput
import re

sql_buffer = ''

for line in fileinput.input():
    sql_buffer += line

sql_buffer = re.sub(
    r'\t\n',  # match tab just before the newline
    r'\t0\n',  # insert 0 between the tab and newline
    sql_buffer
)

print(sql_buffer)
