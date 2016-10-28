import binascii
import os

filename = raw_input("Input filename: ")
file_size = os.stat(filename).st_size


def hex_view():
    with open(filename, 'rb') as fd:
        counter = 0
        output_str = ""

        print "File size: " + str(file_size) + " bytes"

        while counter <= file_size:
            if counter % 16 == 0:
                output_str = ""
                output_str += str(hex(counter)[2:]).zfill(8)+ " || "
            
            byte = fd.read(1)
            output_str += str(binascii.hexlify(byte)) + " "
            
            if counter % 16 == 15:
                print output_str
            
            counter += 1


def hex_edit():
    print "hello"


if __name__ == "__main__":
    hex_view()
