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


2. Аналогично из результатов [10] сложно вынести точный вердикт: есть ЦВЗ или нет в изображении (**stegaatacka/output/**). Например, мы скормим программе файл без ЦВЗ **1.png**, но программа что-то нашла:

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/A1.png)

Допустим, а что она скажет тогда для заполненного текстом контейнера **new.png**?

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Anew.png)

Тоже самое, ну а для вложения картинки в картинку?

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Apic2in1.png)

Ну хоть какое-то отличие, но вряд ли это однозначное определение, т.к. слишком малая разница (*статистическая значимость вообще есть?* ~~не, не слышал~~) 
Для частотного внедрения результаты "чуть получше", но однозначного заключения по ним я бы делать однозначно не стал:)  Потому что -- берём пустой контейнер:

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Are2.png)

А потом частотно-заполненный другим изображением:

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Aembedded_img.png)

кажется, что мы изображения для анализа перепутали, но нет, примерно таже картина при частотно-текстовом заполнении:

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Aembedded_text.png)

А потом повредили контейнер (текст мы можем извлечь, как показано в предыдущем репо [12]), а вот обнаружить внедрение ЦВЗ этим инструментов уже, видимо, нет.

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/Aembedded_text1.png)

3. [9] имеет только CLI, но да ладно, а что по результатам сравнения? Тоже нет однозначного заключения по результатам разных метрик:


$ python3 stegmachine.py --analysis spa new.png output (контейнер с текстом)  
INFO     [2023-10-26 11:29:17,789] Calculating spa beta for new.png ...🌀  
INFO     [2023-10-26 11:29:21,239] SPA estimate for new.png is 0.02431179113635226  


$ python3 stegmachine.py --analysis spa 1.png output (пустой контейнер)  
INFO     [2023-10-26 11:30:35,925] Calculating spa beta for 1.png ...🌀  
INFO     [2023-10-26 11:30:39,449] SPA estimate for 1.png is 0.024313585065328634  


$ python3 stegmachine.py --analysis rs 1.png output (пустой контейнер)  
INFO     [2023-10-26 11:31:22,868] Calculating rs estimate for 1.png ...🌀   
INFO     [2023-10-26 11:31:37,613] RS estimate for 1.png is 0.013611655019081436  


$ python3 stegmachine.py --analysis rs new.png output (контейнер с текстом)  
INFO     [2023-10-26 11:31:51,781] Calculating rs estimate for new.png ...🌀  
INFO     [2023-10-26 11:32:06,292] RS estimate for new.png is 0.013617516656435286  


python3 stegmachine.py --analysis visual -j new.png output (контейнер с текстом) 

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/output/LSB-new.bmp)

python3 stegmachine.py --analysis rs  tinne-7-with-hidetext.jpeg output (контейнер с текстом) 
INFO     [2023-10-26 11:50:49,349] RS estimate for tinne-7-with-hidetext.jpeg is 0.002579826565077244

$ python3 stegmachine.py --analysis rs  tinne-7.jpeg output (пустой контейнер)  
INFO     [2023-10-26 11:51:23,916] RS estimate for tinne-7.jpeg is 0.002579826565077244


python3 stegmachine.py --analysis spa  tinne-7-with-hidetext.jpeg output (контейнер с текстом)   
INFO     [2023-10-26 11:52:16,905] SPA estimate for tinne-7-with-hidetext.jpeg is 0.004610292944580677  


$ python3 stegmachine.py --analysis spa  tinne-7.jpeg output (пустой контейнер)  
INFO     [2023-10-26 11:52:32,839] SPA estimate for tinne-7.jpeg is 0.004610292944580677  


$ python3 stegmachine.py --analysis spa  re2.png output (пустой контейнер)    
INFO     [2023-10-26 11:53:47,146] SPA estimate for re2.png is 0.01116957010861  


$ python3 stegmachine.py --analysis spa  embedded_text.png output (контейнер с текстом)  
INFO     [2023-10-26 11:54:18,967] SPA estimate for embedded_text.png is 0.0029202760186748822  


$ python3 stegmachine.py --analysis spa  embedded_text.jpg output (контейнер с текстом)   
INFO     [2023-10-26 11:54:31,118] SPA estimate for embedded_text.jpg is 0.01194868518796146  


$ python3 stegmachine.py --analysis spa  embedded_img.png output (контейнер с qr-изображением)   
INFO     [2023-10-26 11:54:49,633] SPA estimate for embedded_img.png is 0.007523952658835668  


$ python3 stegmachine.py --analysis rs re2.png output (пустой контейнер)  
INFO     [2023-10-26 11:56:17,821] RS estimate for re2.png is -0.014033537220522937  


$ python3 stegmachine.py --analysis rs embedded_text.png output (контейнер с текстом)  
INFO     [2023-10-26 11:56:46,344] RS estimate for embedded_text.png is -0.022121029378369114  


$ python3 stegmachine.py --analysis rs embedded_text.jpg output (контейнер с текстом) 
INFO     [2023-10-26 11:57:06,395] RS estimate for embedded_text.jpg is 0.0030612676420325637  

$ python3 stegmachine.py --analysis rs embedded_img.png output  
INFO     [2023-10-26 11:57:40,517] RS estimate for embedded_img.png is -0.0016789800292105084  


Опять не всё так однозначно -- отличия не столь существенные для строгого заключения  о наличии внедрения ЦВЗ.  


4. #### Энтропия изображения


Энтропия измеряет информационное содержание изображения, используемое при обработке изображений. Высокое значение энтропии обозначает сложное изображение с широким диапазоном значений пикселей, в то время как низкое значение энтропии обозначает более простое и однородное изображение. Энтропия может быть использована для оценки качества или сложности изображения и поиска наиболее информативных частей изображения для дальнейшей обработки или анализа [13].  


Попробуем посчитать величину энтропии для пустого и заполненного контейнеров в наших методах внедрения ЦВЗ **entro.py**. Вот результаты и некоторые гистограммы (остальные в папке     **stegaatacka/img/**):  


Image Entropy 6.884162225879558 for 1.png  
Image Entropy 6.884168387506503 for new.png  (контейнер с текстом)  


Image Entropy 6.878406945299694 for tinne-7.jpeg  
Image Entropy 6.878406945299694 for tinne-7-with-hidetext.jpeg  (контейнер с текстом)  


Image Entropy 3.639428204549869 for re2.png  

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/ImageEntropy_re2.png.png)

Image Entropy 3.6975179459936514 for embedded_text.png  (контейнер с текстом)  

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/ImageEntropy_embedded_text.png.png)

Image Entropy 3.713204815625096 for embedded_text.jpg  (контейнер с текстом)  
Image Entropy 4.8650606316696425 for embedded_img.png  (контейнер с qr-изображением)

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/ImageEntropy_embedded_img.png.png)

Image Entropy 0.046919139587702725 for embedded_text1.png  (повреждённый контейнер с текстом с вырезанной частью в графредакторе)  

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/ImageEntropy_embedded_text1.png.png)


Image Entropy 0.38195800357484044 for 7corupt.png 


Image Entropy 0.8511453835607288 for watermark_qrcode.png  
Image Entropy 0.96557866684501 for watermark_qrcode (2-я извлёк).png  
Image Entropy 5.807410296979399 for watermark_qrcode()извлёк после телеги.jpg    


Энтропия контейнера слегка повышается при частотном внедрении текста и чуть больше при частотном внедрении изображения, но нечувствительна к топорному битовому и LSB-внедрению. К тому же при частотном внедрении текста в иображение её величину можно лекго изменить, если вырезать какую-нибудь подходящую часть (а передаваемый текст, напомню, не пострадает). отсюда вывод: сей подход не поможет в реальной практике.


## Вывод

1. Представленные для широкой общественности в интернет-пространстве инструменты по выявлению внедрения ЦВЗ и стегосообщений либо устарело и не может быть запущено, либо не даёт какого-то реально значимого результата.
2. Может быть существует спецсофт для профорганизаций, но об этом у нас нет данных.
3. Возможно стоит посмотреть в сторону нейросетевых решений.

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
12. [Ma3shka](https://github.com/unton3ton/Ma3shka)
13. [A Complete Guide to Picture Complexity Assessment Using Entropy](https://unimatrixz.com/blog/latent-space-image-quality-with-entropy/)
