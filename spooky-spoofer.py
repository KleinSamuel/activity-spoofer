#!/usr/bin/python3

import os, time

magic_file = "magic-file.txt"

with open(magic_file, "w") as file:
    timestamp = time.time()
    file.write(str(timestamp))

os.system("git add "+magic_file)

os.system("git commit -m 'magic happened again'")

os.system("git push")