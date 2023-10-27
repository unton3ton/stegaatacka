from PIL import Image, ImageChops

"""
image_1=Image.open('1.jpg')
image_2=Image.open('2.jpg')

result=ImageChops.difference(image_1, image_2)
#result.show()

#Вычисляет ограничивающую рамку ненулевых областей на изображении.
print(result.getbbox()) 

# result.getbbox() в данном случае вернет (0, 0, 888, 666)
result.save('result.jpg')
"""


def difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    
    # size = [400,300]        #размер в пикселях
    # image_1.thumbnail(size) #уменьшаем первое изображение
    # image_2.thumbnail(size) #уменьшаем второе изображение

    #сравниваем уменьшенные изображения
    result=ImageChops.difference(image_1, image_2)
    
    print(result.getbbox()) 
    
    result.save('pillow-diff-result-frequency.png')

difference_images('re2.png','embedded_text.png') # ValueError: images do not match аналогично для LSB
# compare tinne-7.jpeg tinne-7-with-hidetext.jpeg compare-diffimage-tine.jpeg # мало отличий
# compare 1.png new.png compare-diffimage-LSB.png # мало отличий
# compare re2.png embedded_text.png compare-diffimage-frequency.png # много отличий

# md5sum tinne-7.jpeg tinne-7-with-hidetext.jpeg # много отличий
# 7790d473d73696b6b91f6848bfe1afa6  tinne-7.jpeg
# 46b143a84c157a6fe2fdd6c6c73d8888  tinne-7-with-hidetext.jpeg

# $ cmp -l tinne-7.jpeg tinne-7-with-hidetext.jpeg | gawk '{printf "%08X %02X %02X\n", $1-1, strtonum(0$2), strtonum(0$3)}' > diff_tinne.txt
# $ cmp: EOF в tinne-7.jpeg после байта 121465

# diff -y <(xxd tinne-7.jpeg) <(xxd tinne-7-with-hidetext.jpeg) > diffhex-tinne.txt # находит отличающиеся строки в конце файла, где и записывали

# diff -y <(xxd 1.png) <(xxd new.png) > diffhex-LSB.txt # находит отличающиеся строки по всему файлу (полностью разные файлы)

# diff -y <(xxd re2.png) <(xxd embedded_text.png) > diffhex-frequency.txt # находит отличающиеся строки по всему файлу (полностью разные файлы)

# $ md5sum re2.png embedded_text.png 
# 4e07744be4da456297a6dc99d69cac6c  re2.png
# a735eb4849c5b22e9b4cac22a687ad75  embedded_text.png
