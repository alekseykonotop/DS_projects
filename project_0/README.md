# Проект 0. Игра угадай число.

## Оглавление
[1. Описание проекта](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результаты](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Результаты)  
[6. Выводы](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Выводы)


### Описание проекта
Угадать загаданное компьютером число за минимальное кол-во попыток.


### Какой кейс решаем?
**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. 
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.  
  
**Метрика качества**  
Результаты оцениваются по среднему кол-ву попыток при 1000 повторений. 

**Что практикуем**  
Учимся писать хороший код на Python


### Краткая информация о данных
Данные не передаются, так как генерируются рандомно функцией тестирования алгоритма поиска.  


### Этапы работы над проектом
1. Реализовали примитивные алгоритм угадывания числа рандомным способом.  
2. Улучшили алгоритм добавив смещение в предсказанию.  
3. Реализовали алгоритм предсказания на основе рекурсивного поиска. 


### Результаты  
Первые 2 версии алгорима угадывали предсказанное число крайне не эффективно, в среднем за 102 и 22 попытки соответственно.  
Рекурсивный алгоритм бинарного поиска показал самый лучший результат, равный в среднем 5 попыткам. 


### Выводы
Используя алгоритм бинарного поиска реализовано нахождение загаданного числа в среднем за 5 попыток.  
Среднее значение получено на основе 1000 наблюдений.  
Данное решение удовлетворяет условию: угадывает число меньше, чем за 20 попыток.  
Здача решена.  
  

:arrow_up:[к оглавлению](https://github.com/alekseykonotop/DS_projects/blob/main/project_0/README.md#Оглавление)
