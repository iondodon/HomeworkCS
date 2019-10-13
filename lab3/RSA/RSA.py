p = 17
q = 29

n = p * q

phi_n = (p - 1) * (q - 1)


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


e = phi_n - 1
while gcd_eea([e, phi_n])[0] != 1 and e > 1:
    e -= 1


print(e)
