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