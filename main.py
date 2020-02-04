#!/usr/bin/env python3

import os
import argparse
from PIL import Image

### Make DIR a cmd line argument
### Make Resizing a CMD line argument
#directory = ('/home/sos/Desktop/Earth/earthtimelapse/') ### MANUAL METHOD

import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--rate", default=1, type=float, help="This is the resize variable variable")
parser.add_argument("--origin", required=True, type=str, help="origin dir")
parser.add_argument("--dest", type=str, help="dest dir")
parser.add_argument("--type", type=str)

args = parser.parse_args()
rate = args.rate
origin = args.origin
dest = args.dest
type= args.type
directory=origin

try:
	os.mkdir(directory + 'resize')
except os.error as e:
	print (e + directory + '/resize  creation has failed')
except:
	print (directory + '/resize has been created')


for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(type):
         print(os.path.join(directory, filename))
         foo = Image.open(directory + filename)
         h, w = foo.size
         print('width: ', w)
         print('height:', h)
         foo = foo.resize((int(h*rate),int(w*rate)),Image.ANTIALIAS) #######<<<< CHANGE THE RES TO WHAT WE NEED!!
         foo.save(directory + 'resize/' + "scaled_" + filename + type,quality=95)

         continue
     else:
         continue
