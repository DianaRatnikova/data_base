# data_base
Выполнен 1ый трек по безем данных LearnPython



## Сборка репозитория и локальный запуск
Выполните в консоли:
```
git clone https://github.com/DianaRatnikova/data_base
pip install -r requirments.txt
```
 
### Создание базы данных
Создайте БД на ElephantSQL, откройте её в ValentinaStudio
```
https://customer.elephantsql.com/instance
https://www.valentina-db.com/
```

### Создание базы данных
Из корня проекта запустите конструктор базы данных:
```
python models.py
```

### Запуск
Для добавления записи в таблицу запустите из корня проекта:
```
python add_user.py
```
Для получения первой по очереди записи таблицы запустите из корня проекта:
```
python get_user.py
```
Для обновления/изменения записи таблицы запустите из корня проекта:
```
python update_user.py
```
Для удаления записи таблицы запустите из корня проекта:
```
python delete_user.py
```

