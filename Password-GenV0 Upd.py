import secrets
import string

def generate_hex_password(length=16):
    hex_chars = string.hexdigits.lower()  # '0123456789abcdefABCDEF', берем только нижний регистр
    # Формируем пароль, выбирая случайные символы из hex_chars
    password = ''.join(secrets.choice(hex_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Введите длину шестнадцатеричного пароля: "))
    password = generate_hex_password(length)
    print("Сгенерированный пароль:", password)
