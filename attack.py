# python3 -m venv ATTAK
# source ATTAK/bin/activate

# pip install --upgrade pip
# pip install Pillow
# pip install ImageHash
# pip install PyExifTool
# pip install numpy
# pip install scipy

# deactivate


import PIL
from PIL import Image
import imagehash

image_1 = Image.open('re2.png')
image_2 = Image.open('embedded_text.png')


hash1 = imagehash.phash(image_1)
print(hash1)

hash2 = imagehash.phash(image_2)
print(hash2)

print(hash1 == hash2)

print(hash1 - hash2)

# ('re2.png') ('embedded_text.png')
# f6b4926217d0ac6e
# f6b492661791cc6a
# False
# 6

# tinne-7.jpeg tinne-7-with-hidetext.jpeg
# 94d4a463eb4ce60f
# 94d4a463eb4ce60f
# True
# 0

# 1.png new.png
# ff91c1b233478dc0
# ff91c1b233478dc0
# True
# 0



"""
stegolsb stegdetect -i tinne-7.png -n 2
stegolsb stegdetect -i simple-result.png -n 2
"""


"""
python3 stegmachine.py --analysis spa new.png output
INFO     [2023-10-26 11:29:17,789] Calculating spa beta for new.png ...🌀
INFO     [2023-10-26 11:29:21,239] SPA estimate for new.png is 0.02431179113635226

python3 stegmachine.py --analysis spa 1.png output
INFO     [2023-10-26 11:30:35,925] Calculating spa beta for 1.png ...🌀
INFO     [2023-10-26 11:30:39,449] SPA estimate for 1.png is 0.024313585065328634

python3 stegmachine.py --analysis rs 1.png output
INFO     [2023-10-26 11:31:22,868] Calculating rs estimate for 1.png ...🌀
INFO     [2023-10-26 11:31:22,868] It will take a couple of minutes...
INFO     [2023-10-26 11:31:37,613] RS estimate for 1.png is 0.013611655019081436

$ python3 stegmachine.py --analysis rs new.png output
INFO     [2023-10-26 11:31:51,781] Calculating rs estimate for new.png ...🌀
INFO     [2023-10-26 11:31:51,782] It will take a couple of minutes...
INFO     [2023-10-26 11:32:06,292] RS estimate for new.png is 0.013617516656435286

python3 stegmachine.py --analysis visual new.png output
INFO     [2023-10-26 11:35:12,267] Visualising lsb for new.png ...🌀
INFO     [2023-10-26 11:35:14,631] Openning red component...🌀
INFO     [2023-10-26 11:35:17,497] Openning green component...🌀
INFO     [2023-10-26 11:35:20,306] Openning blue component...🌀

python3 stegmachine.py --analysis visual -j new.png output
"""

"""
python3 stegmachine.py --analysis rs  tinne-7-with-hidetext.jpeg output
INFO     [2023-10-26 11:50:28,802] Calculating rs estimate for tinne-7-with-hidetext.jpeg ...🌀
INFO     [2023-10-26 11:50:28,802] It will take a couple of minutes...
INFO     [2023-10-26 11:50:49,349] RS estimate for tinne-7-with-hidetext.jpeg is 0.002579826565077244

$ python3 stegmachine.py --analysis rs  tinne-7.jpeg output
INFO     [2023-10-26 11:51:03,523] Calculating rs estimate for tinne-7.jpeg ...🌀
INFO     [2023-10-26 11:51:03,523] It will take a couple of minutes...
INFO     [2023-10-26 11:51:23,916] RS estimate for tinne-7.jpeg is 0.002579826565077244


python3 stegmachine.py --analysis spa  tinne-7-with-hidetext.jpeg output
INFO     [2023-10-26 11:52:12,426] Calculating spa beta for tinne-7-with-hidetext.jpeg ...🌀
INFO     [2023-10-26 11:52:16,905] SPA estimate for tinne-7-with-hidetext.jpeg is 0.004610292944580677

$ python3 stegmachine.py --analysis spa  tinne-7.jpeg output
INFO     [2023-10-26 11:52:28,465] Calculating spa beta for tinne-7.jpeg ...🌀
INFO     [2023-10-26 11:52:32,839] SPA estimate for tinne-7.jpeg is 0.004610292944580677
"""

"""
python3 stegmachine.py --analysis spa  re2.png output
INFO     [2023-10-26 11:53:46,768] Calculating spa beta for re2.png ...🌀
INFO     [2023-10-26 11:53:47,146] SPA estimate for re2.png is 0.01116957010861

$ python3 stegmachine.py --analysis spa  embedded_text.png output
INFO     [2023-10-26 11:54:18,586] Calculating spa beta for embedded_text.png ...🌀
INFO     [2023-10-26 11:54:18,967] SPA estimate for embedded_text.png is 0.0029202760186748822

$ python3 stegmachine.py --analysis spa  embedded_text.jpg output
INFO     [2023-10-26 11:54:30,752] Calculating spa beta for embedded_text.jpg ...🌀
INFO     [2023-10-26 11:54:31,118] SPA estimate for embedded_text.jpg is 0.01194868518796146

$ python3 stegmachine.py --analysis spa  embedded_img.png output
INFO     [2023-10-26 11:54:46,346] Calculating spa beta for embedded_img.png ...🌀
INFO     [2023-10-26 11:54:49,633] SPA estimate for embedded_img.png is 0.007523952658835668


python3 stegmachine.py --analysis rs re2.png output
INFO     [2023-10-26 11:56:16,167] Calculating rs estimate for re2.png ...🌀
INFO     [2023-10-26 11:56:16,167] It will take a couple of minutes...
INFO     [2023-10-26 11:56:17,821] RS estimate for re2.png is -0.014033537220522937

$ python3 stegmachine.py --analysis rs embedded_text.png output
INFO     [2023-10-26 11:56:44,652] Calculating rs estimate for embedded_text.png ...🌀
INFO     [2023-10-26 11:56:44,652] It will take a couple of minutes...
INFO     [2023-10-26 11:56:46,344] RS estimate for embedded_text.png is -0.022121029378369114

$ python3 stegmachine.py --analysis rs embedded_text.jpg output
INFO     [2023-10-26 11:57:04,656] Calculating rs estimate for embedded_text.jpg ...🌀
INFO     [2023-10-26 11:57:04,656] It will take a couple of minutes...
INFO     [2023-10-26 11:57:06,395] RS estimate for embedded_text.jpg is 0.0030612676420325637

$ python3 stegmachine.py --analysis rs embedded_img.png output
INFO     [2023-10-26 11:57:25,346] Calculating rs estimate for embedded_img.png ...🌀
INFO     [2023-10-26 11:57:25,346] It will take a couple of minutes...
INFO     [2023-10-26 11:57:40,517] RS estimate for embedded_img.png is -0.0016789800292105084

"""