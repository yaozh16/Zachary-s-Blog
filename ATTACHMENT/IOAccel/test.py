import os
import time
import re
def test(exefile,n):
        print os.popen(exefile+' < data.txt').read(),

os.popen('python gen.py > data.txt')
print "Gen done"
test("build/V1",30)
test("build/V2",30)
test("build/V2",30)
