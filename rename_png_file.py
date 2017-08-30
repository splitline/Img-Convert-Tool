import os
import struct

def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


rootDir = input("Input Root Dir > ")
list_dirs = os.walk(rootDir)
for root, dirs, files in list_dirs:
    for filename in files:
        # print(root+"/"+filename)
        new_filename = filename
        filename = root+"/"+filename
        binfile = open(filename, 'rb')
        hcode = "89504E47" #PNG header
        numOfBytes = len(hcode) // 2
        binfile.seek(0)
        hbytes = struct.unpack_from('B' * numOfBytes, binfile.read(numOfBytes))
        f_hcode = bytes2hex(hbytes)
        for c in new_filename:
            if (u'\u4e00' <= c <= u'\u9fff'):
                new_filename = new_filename.replace(c, "")
        new_filename.strip()
        if f_hcode == hcode and not new_filename.endswith('.png'):
            new_filename = new_filename + ".png"
        if filename != root +"/"+new_filename:
            print("[rename] " + filename)
            os.rename(filename, root +"/"+new_filename)
        binfile.close()
    for d in dirs:
        for c in d:
            if (u'\u4e00' <= c <= u'\u9fff'):
                with open("chinese_dir.txt", "a") as f:
                    f.write(root+"/"+d+"\n")
                break

