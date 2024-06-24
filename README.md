# Лига чемпионов УЕФА

Лига чемпионов УЕФА - один из самых престижных турниров в мире футбола, в котором принимают участие лучшие клубы Европы. Этот набор данных был составлен для того, чтобы проанализировать тенденции, результаты команд и эволюцию игры на протяжении почти семи десятилетий.

В то время как существует множество наборов данных, посвященных отдельным сезонам Лиги чемпионов УЕФА, ощущается заметная нехватка всеобъемлющих наборов данных, охватывающих всю историю турнира. Данный набор данных призван восполнить этот пробел, предоставляя единый ресурс для исторического анализа за весь период проведения соревнований.

Этот дашборд предоставляет обзор данных о финалах Лиги чемпионов УЕФА, включая информацию о победителях, финалистах, посещаемости и месте проведения.

Описание файлов данных:
+ Season: Футбольный сезон, в котором был сыгран финал.
+ Country: Страна победителя.
+ Winners: Название команды-победительницы.
+ Score: Итоговый счет в конце матча.
+ Runners-up: Команда, занявшая второе место.
+ HomeCountry: Страна, в которой находится команда, занявшая второе место.
+ Venue: Место проведения финального матча.
+ Attendance: Количество зрителей, присутствующих в месте проведения матча.
+ Notes: Дополнительная информация, например, перешел ли матч в дополнительное время или какие-либо другие примечательные события.

## Ссылка на датасет
[Champions League Dataset 1955-2023](https://www.kaggle.com/datasets/fardifaalam170041060/champions-league-dataset-1955-2023/data)

## Ссылка на сайт
[Pythonanywhere](http://ivanef.pythonanywhere.com/)

## Как развернуть
1. Скачать Zip-архив с GitHub
2. Установить виртульаное окружение:
    * python -m venv venv
3. Активировать виртульаное окружение:
    * source venv/Scripts/activate
4. Установить необходимые библиотеки с помощью следующих команд:
    * pip install dash pandas
    * pip install dash-bootstrap-components
