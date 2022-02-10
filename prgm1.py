import sys
fp = open(sys.argv[1])
data=fp.read()
para=data.split()
print('total number of words',len(para))