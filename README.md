## Предварительная подготовка

Добавим для опытов ещё один пример стеганографии [1].

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/tinne-7.png)

> ### Видишь разницу между картинками? А она есть! (смотри hex-представление text-with.txt & text-without.txt)

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/tinne-7-with-hidetext.jpeg)

## Поехали!

1. С наскока найти разницу с уже использованным инструментом (правда для совершенно другой задачи) [2] не удалось. Linux-команда *identify*, предоставляющая подробную информацию об изображении, оказалась чуть более, чем бесполезна для выявления внедрения ЦВЗ.  


2. Команда *compare* используется для сравнения двух изображений для обнаружения различий между изображениями, который может быть полезен для контроля качества, тестирования и анализа изображений. Используем её:  


> $ compare tinne-7.jpeg tinne-7-with-hidetext.jpeg compare-diffimage-tine.jpeg -> мало отличий для топорной стеганографии

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare-diffimage-tine.jpeg)

> $ compare 1.png new.png compare-diffimage-LSB.png -> мало отличий для LSB внедрения текста, но есть значительные отличия для внедрения картинки

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare-diffimage-LSB.png)

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare_1.png_pic2in1.png_diff.png)

> $ compare re2.png embedded_text.png compare-diffimage-frequency.png -> много отличий для частотного внедрения

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare-diffimage-frequency-pngjpeg.png)

3. Контрольная сумма данного файла по математическим законам с очень большой вероятностью будет уникальной. Если два файла имеют одинаковую контрольную сумму, то они почти наверняка являются копиями. Здесь *md5sum* указывает, что первый и третий файлы являются копиями друг друга:


$ md5sum image001.jpg image002.jpg image003.jpg  


146b163929b6533f02e91bdf21cb9563 image001.jpg  
63da88b3ddde0843c94269638dfa6958 image002.jpg  
146b163929b6533f02e91bdf21cb9563 image003.jpg  


$ md5sum tinne-7.jpeg tinne-7-with-hidetext.jpeg -> много отличий  
7790d473d73696b6b91f6848bfe1afa6  tinne-7.jpeg  
46b143a84c157a6fe2fdd6c6c73d8888  tinne-7-with-hidetext.jpeg  


$ md5sum re2.png embedded_text.png  
4e07744be4da456297a6dc99d69cac6c  re2.png  
a735eb4849c5b22e9b4cac22a687ad75  embedded_text.png  


Не особо полезный инструмент для данной задачи.


4. Построчная разница также не принесла пользы (см. результаты во вложениях):

$ cmp -l tinne-7.jpeg tinne-7-with-hidetext.jpeg | gawk '{printf "%08X %02X %02X\n", $1-1, strtonum(0$2), strtonum(0$3)}' > diff_tinne.txt    
$ cmp: EOF в tinne-7.jpeg после байта 121465  


$ diff -y <(xxd tinne-7.jpeg) <(xxd tinne-7-with-hidetext.jpeg) > diffhex-tinne.txt # находит отличающиеся строки в конце файла, где и записывали  


$ diff -y <(xxd 1.png) <(xxd new.png) > diffhex-LSB.txt # находит отличающиеся строки по всему файлу (полностью разные файлы)  


$ diff -y <(xxd re2.png) <(xxd embedded_text.png) > diffhex-frequency.txt # находит отличающиеся строки по всему файлу (полностью разные файлы)  




Но решающий недостаток таких методов: необходим оригинал контейнера, что не всегда доступно.

# Sources

1. [Стеганография с Python. Скрытое сообщение на уровне байтов](https://telegra.ph/Steganografiya-s-Python-Skrytoe-soobshchenie-na-urovne-bajtov-08-19)
2. [humashineye/Naive/simple-dif-img.py](https://github.com/unton3ton/humashineye/blob/main/Naive/simple-dif-img.py)
3. [How do I compare binary files in Linux?](https://superuser.com/questions/125376/how-do-i-compare-binary-files-in-linux)
4. []()
5. []()
6. []()
7. []()
8. []()
9. []()
10. []()
11. []()
12. []()
13. []()
