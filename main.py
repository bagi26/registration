import re


def get_input(prompt):
    return input(prompt + ": ")


def validate_gender(gender):
    if gender.upper() in ['М', 'Ж']:
        return gender.upper()
    else:
        raise ValueError("Неправильный пол. Введите М или Ж.")


def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    if pattern.match(email):
        return email
    else:
        raise ValueError("Неверный формат электронной почты")


def validate_password(password):
    if len(password) < 8:
        raise ValueError("Пароль должен быть длиной минимум 8 символов.")
    else:
        return password


first_name = get_input("Введите имя")
last_name = get_input("Введите фамилию")
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
user_data = {
    "first_name": first_name,
    "last_name": last_name,
    "gender": gender,
    "email": email,
    "login": login,
    "password": password
}
print("\nИнформация по пользователю:")
for key, value in user_data.items():
    print(f"{key.title()}: {value}")
