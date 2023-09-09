# 33.1.Final_project_Rostelecom

33.1. Итоговый проект по автоматизации тестирования (PJ-04)
Заказчик передал вам следующее задание:

1.  Протестировать требования.

2.  Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.

3.  Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.

4.  Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. Если дефекты не обнаружены, то подумайте и опишите 3 потенциально возможных дефекта на данном ресурсе.

Приложите ссылку на документ с тест-кейсами, ссылку на GitHub с автотестами, ссылки на баги или документ с описанием этих багов.

Первоначально, мной были протестированы требования Заказчиков, которые имеют расхождения с реальным сайтом. Различия в описанных требованиях и сайте приведены в файле в виде комментариев по ссылке: https://docs.google.com/document/d/1z2QC31-IYkPeQ2CcuRTIaQluHuPONEbZ/edit?usp=sharing&ouid=117569082253345380291&rtpof=true&sd=true

Далее проводилось тестирование пользовательского интерфейса методом позитивного и негативного функционального тестирования c помощью программной библиотеки Selenium .При разработке тест-кейсов были применены следующие техники тест-дизайна: эквивалентное разбиение, анализ граничных значений, таблица принятия решений, диаграмма перехода состояния, попарное тестирование. Список тест-кейсов, чек-лист и баги представлены по ссылке:https://docs.google.com/spreadsheets/d/1qWQ9l6FexMtMsmxvGMjvsypPJmywpNnEBty0l-uES84/edit?usp=sharing

Автотесты представлены в файлах: test_authorization_by_code.py, test_authorization_page.py, test_registration.py 
