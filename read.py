# python3 read.py > text.txt

try:
    cFile = "tinne-7-with-hidetext.jpeg" # input('File name: ')
    with open(cFile, "rb") as r:
        byte = r.read(1)
        k = 0
        while byte:
            byte = r.read(1)
            print(byte)
            k += 1


except FileNotFoundError:
    print("File: " + str(cFile) + "not found!")
    raise SystemExit

else:
    print("\n[+] Number of bytes in the '"+str(cFile)+"': "+str(k))