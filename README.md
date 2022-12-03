# GUI Calculator (desktop)

![vpyqt](https://img.shields.io/badge/python-v3.8-black)
![vpytnon](https://img.shields.io/badge/PyQt5-v5.15-black)

**Калькулятор** для вычисления математических выражений. Поддерживает 6 операций и скобки.

![screenshot](https://i.ibb.co/3yTLgcx/2022-12-02-11-31-25.png)


# Реализация

Вычисление математического выражения проходит в три этапа.

## 1. Парсинг выражения

Для парсинга реализован класс `expression.Expression`, который принимает строку с математическим выражением и разбивает её на последовательность токенов. Токенами являются числа, операторы, скобки, служебные символы. В процессе преобразования происходит валидация выражения.

Валидация гарантирует:

- выходное значение состоит только из допустимых токенов;
- токены числа не имеют более 1 точки;
- первым или последним токеном не может быть оператор;
- два оператора не могут быть рядом.

После парсинга и валидации хранит последовательность токенов в одном из своих полей.

## 2. Преобразование инфиксной нотации в постфиксную

Преобразование реализовано в классе `calculator.PostfixTranslator`. В преобразовании учавствует стек для хранения операторов. Преобразование происходит на основе управляющей таблицы *(табл.№1)*. Верхняя строчка таблицы - читаемый символ последовательности. Левый столбец - токен на вершине стека операторов. Значение таблицы - номера выполняемых функций.

- $ - читаемый символ
- S - стек
- \# - конец строки
- % - деление по модулю
- ^ - возведение в степень

Управляющая таблица (таблица №1):
| |#|(|+|-|*|/|)|^|%|
|-|-|-|-|-|-|-|-|-|-|
|#|6|1|1|1|1|1|5|1|1|
|(|5|1|1|1|1|1|3|1|1|
|+|4|1|2|2|1|1|4|1|1|
|-|4|1|2|2|1|1|4|1|1|
|*|4|1|4|4|2|2|4|1|2|
|/|4|1|4|4|2|2|4|1|2|
|^|4|1|4|4|4|4|4|1|4|
|%|4|1|4|4|2|2|4|1|2|

Функции:

1. Заслать **$** в стек **S** и читать следующий токен.
2. Выдать команду, заслать **$** в стек **S** и читать следующий токен.
3. Читать из **S** и читать следующий токен (для удаления скобок).
4. Выдать команду и читать тот же токен.
5. Закончить с ошибкой.
6. Успешно закончить.

Каждая пункт соответствует функции `calculator.PostfixTranslator.oper[n] (func)`.

После преобразования, результат сохраняется в одном из полей класса.

## 3. Вычисление

Вычисление реализовано в классе `calculator.Calculator`, который наследуется от `calculator.PostfixTranslator`. Для вычислений используется стек и постфиксная последовательность из родителя. После вычисления результат хранится в одном из полей класса `Calculator`.

*Больше о постфиксной нотации и вычислениях:*

- [Обратная польская запись](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C)
- [Инфиксные, префиксные и постфиксные выражения](http://aliev.me/runestone/BasicDS/InfixPrefixandPostfixExpressions.html)


## Интерфейс пользователя

Интерфейс реализован при помощи графического инструмента PyQt5-Designer. 

# Запуск

1. Клонировать или скачать репозиторий.
2. Создать [виртуальное окружение и установить зависимости](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) из `requirements.txt`.
3. Выполнить файл `main.py`.

# Скачать

Для Linux: https://mega.nz/file/CZ4GBaaJ#Tie4eZYn8UnK7On3a6xdT81ai2bfVNdsCkMxqC5HCBk
