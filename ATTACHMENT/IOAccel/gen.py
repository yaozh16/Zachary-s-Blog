#coding=utf-8


import os
import random
import time
def Gen(n):
	for i in range(n):
		print random.randint(1,1<<30)
Gen(1<<20)
