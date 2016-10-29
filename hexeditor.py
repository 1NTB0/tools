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
            # format: print 16 bytes per line
            if counter % 16 == 0:
                output_str = ""
                output_str += str(hex(counter)[2:]).zfill(8)+ " || "
            # format: print byte by byte
            byte = fd.read(1)
            output_str += str(binascii.hexlify(byte)) + " "
            # every 16 bytes change one line
            if counter % 16 == 15:
                print output_str
            
            counter += 1


def hex_edit():
    pos_str = raw_input("Which byte do you want to change (in hex): ")
    c_str = raw_input("Content (in hex): ")
    pos = int(pos_str, 16)
    c = chr(int(c_str,16))
    
    with open(filename, 'r+b') as fd:
        fd.seek(pos)
        fd.write(c)


def auto_patch():
    find_pattern = raw_input("Give me a pattern to find (in hex): ")
    change_pattern = raw_input("Give me a pattern to change (in hex): ")


if __name__ == "__main__":
    hex_view()
    hex_edit()
    hex_view()
