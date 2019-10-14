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


p = 67
q = 61

n = p * q
print('n=' + str(n))

phi_n = (p - 1) * (q - 1)
print('phi_n='+str(phi_n))

e = 3001
print('e='+str(e))

x = 7
print('x='+str(x))

y = power_mod(x, e, n)
print('y='+str(y))

r, s, t = gcd_eea([e, phi_n])
print('r='+str(r)+', s='+str(s)+', t='+str(t))

d = s % phi_n
print('d='+str(d))

x = power_mod(y, d, n)
print('x='+str(x))
