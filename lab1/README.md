# Лабораторная работа 1

## Установка

Проверим установленный Python

<img src="./images/image4.png" width="500px"/>

Создадим `/var/lob/mycontainer/base` для дальнейшей работы

<img src="./images/image1.png"  width="600px"/>


Далее скачаем alpine через архив в /tmp

<img src="./images/image6.png"  width="500px"/>

Распакуем архив в созданную директорию и проверим через `ls /var/lib/mycontainer/base`

<img src="./images/image7.png"  width="500px"/>

## Написание скрипта

В диретктории лабы был создан конфиг `config.json`

<img src="./images/image3.png"  width="500px"/>

Также был создан и написан файл `main.py`, который отвечает за всю логику.

<img src="./images/image2.png"  width="500px"/>

## Запуск

main.py был запущен и в нём были протестированы основные требования (PID, namespace, ls)

<img src="./images/image2.png"  width="500px"/>


## Проверка overlayfs

Для првоерки внутри был создан файл testfile с выходом из контейнера. Этоот файл был найден в директории `/var/lib/mycontainer/test1/upper` - то есть всё сработало

<img src="./images/image5.png" width="500px"/>

