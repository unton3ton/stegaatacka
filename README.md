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


5. Использование Python-библиотеки *ImageHash 4.3.1* [4] (cкрипт **attack.py**) и перцептивного хэша [5] позволил выявить присутствие частотного внедрения, но проигнорировал топорное и LSB:


('re2.png') ('embedded_text.png')  
f6b4926217d0ac6e  
f6b492661791cc6a  
False  
6  


tinne-7.jpeg tinne-7-with-hidetext.jpeg  
94d4a463eb4ce60f  
94d4a463eb4ce60f  
True  
0  


1.png new.png  
ff91c1b233478dc0  
ff91c1b233478dc0  
True  
0  


Но решающий недостаток таких методов: необходим оригинал контейнера, что не всегда доступно.


## Спецрешение

"К чему вообще нужны эти танцы с бубном?"  


Почему бы не использовать профрешение и искать внедрение ЦВЗ с помощью него? Интернет-сёрфинг помог найти такие программы [6,7], но большая часть из них либо давно не обновлялась (последний коммит на гитхаб 10 лет назад), либо просто не запускается (по крайней мере, мне не удалось заставить их работать). Есть и более свежие (а главное запускаемые решения) [8-11], которые не нуждаются в оригинальном изображении для своей работы. Let's go'ушки тестить их!  


1. Сравним результаты "выхлопа" [11] для чистого изображения девушки и костыльно внедрённой видимой ватерматки **simple-watermark.py**:


> $ stegolsb stegdetect -i tinne-7.png -n 2  

<p>
    <img src="https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/tinne-7.png" >
    <img src="https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/tinne-7_2LSBs.png" >
</p>

> $ stegolsb stegdetect -i simple-result.png -n 2  

<p>
    <img src="https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/simple-result.png" >
    <img src="https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/simple-result_2LSBs.png" >
</p>


Конечно заметна некоторая "сглаженность" шума в месте внедрения изображения, но это только на данном примере и при условии, что мы знаем, что есть это внедрение:) Остальные примеры можно посмотреть в папке **stegaatacka/img/**, но они малоинформативны и не так уж однозначны.  


2. Аналогично из результатов [10] сложно вынести точный вердикт: есть ЦВЗ или нетв изображении (**stegaatacka/output/**). Например, мы скормин программе файл без ЦВЗ **1.png**, но программа что-то нашла:

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/A1.png)

Допустим, а что она скажет тогда для заполненного текстом контейнера **new.png**?

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Anew.png)

Тоже самое, ну а для вложения картинки в картинку?

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Apic2in1.png)

Ну хоть какое-то отличие, но вряд ли это однозначное определение, т.к. слишком малая разница (*статистическая значимость вообще есть?* --не, не слышал--)  


# Sources

1. [Стеганография с Python. Скрытое сообщение на уровне байтов](https://telegra.ph/Steganografiya-s-Python-Skrytoe-soobshchenie-na-urovne-bajtov-08-19)
2. [humashineye/Naive/simple-dif-img.py](https://github.com/unton3ton/humashineye/blob/main/Naive/simple-dif-img.py)
3. [How do I compare binary files in Linux?](https://superuser.com/questions/125376/how-do-i-compare-binary-files-in-linux)
4. [pip install ImageHash](https://pypi.org/project/ImageHash/)
5. [«Выглядит похоже». Как работает перцептивный хэш](https://habr.com/ru/articles/120562/)
6. [Обратная сторона стеганографии](https://xakep.ru/2007/04/18/37769/)
7. [3 Free Steganography Detection Software to do Steganalysis on Images](https://www.ilovefreesoftware.com/04/featured/free-steganography-detection-software-steganalysis-images.html)
8. [Скрывать не скрывая. Еще раз о LSB-стеганографии, хи-квадрате и… сингулярности?](https://habr.com/ru/articles/422593/)
9. [StegMachine](https://github.com/Panda-Lewandowski/StegMachine)
10. [Stego Analyzer Версия: 2.1](https://github.com/Ner-Kat/StegoAnalyzer/tree/main) (*sudo apt-get install python3-tk*) *python StegoAnalyzer.py*  
11. [Steganography: Least Significant Bit Steganography for bitmap images (.bmp and .png)](https://github.com/ragibson/Steganography/tree/master) *stegolsb stegdetect -i embedded_text.png -n 2*  
12. []()
13. []()
14. []()
