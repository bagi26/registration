import re
from datetime import datetime


def get_input(prompt):
    return input(prompt + ": ")


def validate_gender(gender):
    if gender.upper() in ['М', 'Ж']:
        return gender.upper()
    else:
        raise ValueError("Неправильный пол. Введите М или Ж.")


def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    if pattern.match(email) and len(email) <= 25:
        return email
    else:
        raise ValueError("Неверный формат электронной почты или длина больше 25 символов")


def validate_password(password):
    if len(password) < 6:
        raise ValueError("Пароль должен быть длиной минимум 6 символов.")
    elif len(password) > 25:
        raise ValueError("Пароль должен быть длиной минимум 25 символов.")
    else:
        return password


def validate_name(field):
    if len(field) > 50 or not field.isalpha():
        raise ValueError("Поле может содержать только буквы и не может быть длинее 50 символов.")
    else:
        return field


def validate_birth_date(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
        if birth_date > datetime.now():
            raise ValueError("Дата рождения не может быть больше текущей даты")
        return birth_date.strftime("%d-%m-%Y")
    except ValueError:
        raise ValueError("Неверный формат даты. Используйте ДД-ММ-ГГГГ.")


while True:
    first_name = get_input("Введите имя")
    try:
        first_name = validate_name(first_name)
        break
    except ValueError as e:
        print(e)
while True:
    last_name = get_input("Введите фамилию")
    try:
        last_name = validate_name(last_name)
        break
    except ValueError as e:
        print(e)
while True:
    city = get_input("Введите город")
    try:
        city = validate_name(city)
        break
    except ValueError as e:
        print(e)
while True:
    birth_date_str = get_input("Введите свою дату рождения (ДД-ММ-ГГГГ)")
    try:
        birth_date = validate_birth_date(birth_date_str)
        break
    except ValueError as e:
        print(e)
while True:
    gender = get_input("Введите пол (М/Ж)")
    try:
        gender = validate_gender(gender)
        break
    except ValueError as e:
        print(e)
while True:
    email = get_input("Введите e-mail")
    try:
        email = validate_email(email)
        break
    except ValueError as e:
        print(e)
login = get_input("Введите логин")
while True:
    password = get_input("Введите пароль")
    try:
        password = validate_password(password)
        break
    except ValueError as e:
        print(e)
while True:
    repeat_password = get_input("Повторите пароль")
    if password == repeat_password:
        break
    else:
        print("Пароли не совпадают. Попробуйте еще раз.")
if not first_name or not last_name or not gender or not email or not password or not repeat_password or not login:
    raise ValueError("Все поля являются обязательными.")
user_data = {
    "Имя": first_name,
    "Фамилия": last_name,
    "Пол": gender,
    "Электронная почта": email,
    "Логин": login,
    "Пароль": password,
    "Город": city,
    "Дата рождения": birth_date
}
print("\nИнформация по пользователю:")
for key, value in user_data.items():
    print(f"{key.title()}: {value}")
