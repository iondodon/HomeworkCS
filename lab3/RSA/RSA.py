def gcd_eea(r):
    s = [1, 0]
    t = [0, 1]
    i = 1

    while r[i] != 0:
        i = i + 1
        r.append(r[i-2] % r[i-1])
        q = (r[i-2] - r[i]) // r[i-1]
        s.append(s[i-2] - q * s[i-1])
        t.append(t[i-2] - q * t[i-1])

    return r[i-1], s[i-1], t[i-1]


def power_mod(b, p, n):
    result = 1

    while p > 0:
        if p % 2 == 0:
            b = (b * b) % n
            p = p // 2
        else:
            result = (result * b) % n
            p = p - 1

    return result


print(power_mod(9, 9, 4))
print(9**9)

p = 3
q = 11

n = p * q

phi_n = (p - 1) * (q - 1)

e = 3
print(e)

r, s, t = gcd_eea([e, phi_n])
d = s % phi_n
print(d)
