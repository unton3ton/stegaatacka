try:
    cFile = "tinne-7-with-hidetext.jpeg" # input('File name: ')
    with open(cFile, "ab") as file:
        text = "QR codes contain more complex information than just text. Need used special data formats: vCard, iCalendar." # input('Write your text: ')
        file.write(text.encode("utf-8"))

except FileNotFoundError:
    print("File: " + cFile + "not found!")
    raise SystemExit

else:
    print("\n[+] Number of bytes in the '"+str(cFile))


"""
Незначительно меняется размер файла:

$ identify tinne-7.jpeg 
$ tinne-7.jpeg JPEG 1080x1350 1080x1350+0+0 8-bit sRGB 121465B 0.000u 0:00.000

$ identify tinne-7-with-hidetext.jpeg 
$ tinne-7-with-hidetext.jpeg JPEG 1080x1350 1080x1350+0+0 8-bit sRGB 121572B 0.000u 0:00.000

"""