# <center>Проект: ИССЛЕДОВАНИЕ ДАННЫХ HR-АГЕНТСТВА</center>

## Оглавление  
[1. Описание проекта](https://github.com/alekseykonotop/DS_projects/blob/main/project_3/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/alekseykonotop/DS_projects/blob/main/project_3/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/alekseykonotop/DS_projects/blob/main/project_3/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/alekseykonotop/DS_projects/blob/main/project_3/README.md#Этапы-работы-над-проектом)  
[5. Выводы](https://github.com/alekseykonotop/DS_projects/blob/main/project_3/README.md#Выводы)

### 1. Описание проекта  
Работа с табличными данными:  
- преобразование данных  
- очистка данных 
- разведывательный данных  
- визуализация данных  
- статистические тесты
 

### 2. Какой кейс решаем?  
HR-агентство изучает тренды на рынке труда в IT. Компания хочет провести исследование на основе данных о зарплатах в сфере Data Science за 2020–2022 годы и получить некоторые выводы.  

### 3. Краткая информация о данных  
[Скачать данные для проекта](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9e84f30c5bc84881a5e33262d5e32a8b/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/ds_salaries.zip)  
Оригинальный датасет: [Data Science Job Salaries” (kaggle.com)](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)

**ОПИСАНИЕ ПРИЗНАКОВ**
| НАИМЕНОВАНИЕ СТОЛБЦА  | ОПИСАНИЕ |
| :---          |     :---     |
| `work_year`  | Год, в котором была выплачена зарплата. |
| `experience_level`  | Опыт работы на этой должности в течение года со следующими возможными значениями: |  
|    | - *`EN` — Entry-level/Junior*; |
|    | - *`MI` — Mid-level/Intermediate*; |
|    | - *`SE` — Senior-level/Expert*; |
|    | - *`EX` — Executive-level/Director*.|
| `employment_type`  | Тип трудоустройства для этой роли:  |
|   | - *`PT` — неполный рабочий день*;  |
|   | - *`FT` — полный рабочий день;*  |
|   | - *`CT` — контракт;*  |
|   | - *`FL` — фриланс.*  |
| `job_title`  | Роль, в которой соискатель работал в течение года.  |
| `salary`  | Общая выплаченная валовая сумма заработной платы.  |
| `salary_currency`  | Валюта выплачиваемой заработной платы в виде кода валюты ISO 4217.  |
| `salary_in_usd`  | Зарплата в долларах США (валютный курс, делённый на среднее значение курса доллара США за соответствующий год через fxdata.foorilla.com).  |
| `employee_residence`  | Основная страна проживания сотрудника в течение рабочего года в виде кода страны ISO 3166.  |
| `remote_ratio`  | Общий объём работы, выполняемой удалённо. Возможные значения:  |
|   | - *`0` — удалённой работы нет (менее 20 %);*  |
|   | - *`50` — частично удалённая работа;*  |
|   | - *`100` — полностью удалённая работа (более 80 %).*  |
| `company_location`  | Страна главного офиса работодателя или филиала по контракту в виде кода страны ISO 3166.  |
| `company_size`  | Среднее количество людей, работавших в компании в течение года:  |
|   | - *`S` — менее 50 сотрудников (небольшая компания);*  |
|   | - *`M` — от 50 до 250 сотрудников (средняя компания);*  |
|   | - *`L` — более 250 сотрудников (крупная компания).*  |


### 4. Этапы работы над проектом  
1. Базовый анализ структуры данных;
2. Преобразование данных;
3. Разведывательный анализ - EDA;
4. Ответы на вопросы бизнеса.
  
### 5. Выводы  
Третий data science проект завершен, в рамках которого на практике были выполнены основные этапы работы на основе данных о зарплатах в сфере Data Science за 2020–2022 годы, а именно:  
- чтение данных
- базовый анализ структуры данных  
- преобразование данных  
- разведывательный анализ EDA 
- аггрегирование и визуализация  
- постановка и проверки гипотез на достоверность  
- проведение статистических тестов для колличественных и категориальных признаков



