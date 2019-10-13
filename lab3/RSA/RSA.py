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
    if p == 0:
        return 1
    elif p == 1:
        return b
    elif p % 2 == 1:
        return b * power_mod(b, p - 1, n)
    else:
        return power_mod(b * b, p // 2, n)


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
