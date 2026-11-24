import math
import secrets


def save_keys(public_key, private_key):
    e, n = public_key
    d, _ = private_key

    with open("public.key", "w") as f:
        json.dump({"e": e, "n": n}, f)

    with open("private.key", "w") as f:
        json.dump({"d": d, "n": n}, f)

def load_public_key():
    with open("public.key", "r") as f:
        data = json.load(f)

    return (data["e"], data["n"])


def load_private_key():
    with open("private.key", "r") as f:
        data = json.load(f)

    return (data["d"], data["n"])

def is_prime(n):
    if n < 2 :
        return False
    
    for i in range(2 , math.isqrt(n) + 1):
        if n % i == 0:
            return False
            
    return True


def genelat_prime():
    while True :
        number = 100 + secrets.randbelow(401)

        if is_prime(number):
            return number

def generate_keys():
    p = genelat_prime()
    q = genelat_prime()

    while p == q:
        q = genelat_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if not (1 < e < phi and math.gcd(e, phi) == 1):
        e = 3

    while e < phi and math.gcd(e, phi) != 1:
        e += 2
    if e >= phi:

        raise ValueError("公開指数eが見つかりません")
    d = pow(e, -1, phi)

    pub_key = (e, n)
    pri_key = (d, n)

    return pub_key, pri_key

def encrypt(message, public_key):
    e, n = public_key
    if not 0 <= message < n:
        raise ValueError("メッセージは0以上n未満にしてください")
    return pow(message, e, n)


def decrypt(cipher, private_key):
    d, n = private_key
    if not 0 <= cipher < n:
        raise ValueError("暗号文は0以上n未満にしてください")
    return pow(cipher, d, n)


def text_to_numbers(text):
    numbers = []

    for char in text:
        if not char.isascii():
            raise ValueError("ASCII文字のみ")

        numbers.append(ord(char))

    return numbers
def numbers_to_text(numbers):
    change_num_text = []

    for number in numbers:
        change_num_text.append(chr(number))

    return "".join(change_num_text)

def encrypt_text(text, public_key):
    numbers = text_to_numbers(text)
    encrypted = []

    for number in numbers:
        encrypted.append(enct(number, public_key))

    return encrypted


def decrypt_text(cipher_numbers, private_key):
    decrypted = []

    for cipher in cipher_numbers:
        decrypted.append(dect(cipher, private_key))
    decrypted = numbers_to_text(decrypted)
    
    return decrypted

if __name__ == "__main__":
    public_key, private_key = generate_keys()

    message = "Hello World"
    numbers = text_to_numbers(message)
    decoded = numbers_to_text(numbers)
    print("公開鍵:", public_key)
    print("秘密鍵:", private_key)
    print("元の数値:", message)
    print("暗号文:", numbers)
    print("復号結果:", decoded)
