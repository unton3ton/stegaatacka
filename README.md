## Предварительная подготовка

Добавим для опытов ещё один пример стеганографии [1].

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/tinne-7.png)

> ### Видишь разницу между картинками? А она есть! (смотри hex-представление text-with.txt & text-without.txt)

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/tinne-7-with-hidetext.jpeg)

## Поехали!

С наскока найти разницу с уже использованным инструментом (правда для совершенно другой задачи) [2] не удалось. Linux-команда *identify*, предоставляющая подробную информацию об изображении, оказалась чуть более, чем бесполезна для выявления внедрения ЦВЗ.  


Команда *compare* используется для сравнения двух изображений для обнаружения различий между изображениями, который может быть полезен для контроля качества, тестирования и анализа изображений. Используем её:  


> $ compare tinne-7.jpeg tinne-7-with-hidetext.jpeg compare-diffimage-tine.jpeg -> мало отличий для топорной стеганографии

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare-diffimage-tine.jpeg)

> $ compare 1.png new.png compare-diffimage-LSB.png -> мало отличий для LSB внедрения текста, но есть значительные отличия для внедрения картинки

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare-diffimage-LSB.png)

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare_1.png_pic2in1.png_diff.png)

> $ compare re2.png embedded_text.png compare-diffimage-frequency.png -> много отличий для частотного внедрения

![](https://raw.githubusercontent.com/unton3ton/stegaatacka/main/img/compare-diffimage-frequency-pngjpeg.png)

Но недостаток таких методов: необходим оригинал контейнера, что не всегда доступно.

# Sources

1. [Стеганография с Python. Скрытое сообщение на уровне байтов](https://telegra.ph/Steganografiya-s-Python-Skrytoe-soobshchenie-na-urovne-bajtov-08-19)
2. [humashineye/Naive/simple-dif-img.py](https://github.com/unton3ton/humashineye/blob/main/Naive/simple-dif-img.py)
3. []()
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
