#! /usr/bin/python

__author__ = "Xiaofan (Fred) Jiang"
__copyright__ = "Copyright 2016, Columbia ICSL"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "jiang@ee.columbia.edu"
__status__ = "Production"

"""
Example: 
    hotcrp2acm.py input.json output.csv
"""
import json
import csv
import string
import sys

ofile  = open(sys.argv[2], "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

myfile = open(sys.argv[1], "r")
jsonstr = myfile.read()
data = json.loads(jsonstr)

for x in data:
    row = ["Demo"]
    row.append(x['title'].encode("utf-8"))
    
    t = ""
    for y in x['authors']:
        t = t + y['first'].encode("utf-8") + " " + y['last'].encode("utf-8") + ":" + y['affiliation'].encode("utf-8") + ";"
    t = t[:-1]
    row.append(t)
    
    row.append(x['authors'][0]['email'].encode("utf-8"))
    
    t = ""
    for i in range(1,len(x['authors'])):
        if x['authors'][i].has_key('email'):
            t = t + x['authors'][i]['email'].encode("utf-8")+";"
        else:
            t = t + ";"
    t = t[:-1]
    row.append(t)

    # for line in row:
    #     print line
    writer.writerow(row)
    
print "Finished conversion successfully!"
ofile.close()


    
    



