#!/usr/bin/env python
#Authors : FebraS <sekda@febra.my.id>

import argparse
import qrcode
import string
import random

parser = argparse.ArgumentParser(description="QR Code Generator")

parser.add_argument('-g','--generate',type=str,help='Generate QR Code',required=True)
parser.add_argument('-o','--output',type=str,help='Default QR Ouput Name : \"ScanMe\"',required=False)
args = parser.parse_args()

def qrGenerate(generate,output):
    letters = string.ascii_letters
    letters = ''.join(random.choice(letters)for i in range(10))
    
    qr = qrcode.make(generate)
    if output is not None:
        qr.save("output/"+ output + ".png")
    else:
        qr.save("output/"+ letters +".png")
        print("Your QR are Your QR Code has been created with the name "+ letters +".png")

def main():
    qrGenerate(args.generate,args.output)

main()
