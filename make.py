# coding: utf-8

import os, shutil

os.mkdir('male')
os.mkdir('female')

f = open('name_list.txt')
for line in f:
	line_list = line.split()
	shutil.copy(line_list[1], line_list[0])
f.close()