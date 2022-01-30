import io
import os

import vision_demo


print("__Invoice OCR Scanner__\n")
print("Have working JPEG or PNG invoice file in current directory")

file =  ""
while(file != "exit"):
    file = input("Enter Invoice file Directory:: \n")

    if(file != "exit"):
        vision_demo.main_call(file)