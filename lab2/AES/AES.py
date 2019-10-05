import sys

s_box = {
    '0': {'0': 0x63, '1': 0x7C, '2': 0x77, '3': 0x7B, '4': 0xF2, '5': 0x6B, '6': 0x6F, '7': 0xC5, '8': 0x30, '9': 0x01, 'a': 0x67, 'b': 0x2B, 'c': 0xFE, 'd': 0xD7, 'e': 0xAB, 'f': 0x76},
    '1': {'0': 0xCA, '1': 0x82, '2': 0xC9, '3': 0x7D, '4': 0xFA, '5': 0x59, '6': 0x47, '7': 0xF0, '8': 0xAD, '9': 0xD4, 'a': 0xA2, 'b': 0xAF, 'c': 0x9C, 'd': 0xA4, 'e': 0x72, 'f': 0xC0},
    '2': {'0': 0xB7, '1': 0xFD, '2': 0x93, '3': 0x26, '4': 0x36, '5': 0x3F, '6': 0xF7, '7': 0xCC, '8': 0x34, '9': 0xA5, 'a': 0xE5, 'b': 0xF1, 'c': 0x71, 'd': 0xD8, 'e': 0x31, 'f': 0x15},
    '3': {'0': 0x04, '1': 0xC7, '2': 0x23, '3': 0xC3, '4': 0x18, '5': 0x96, '6': 0x05, '7': 0x9A, '8': 0x07, '9': 0x12, 'a': 0x80, 'b': 0xE2, 'c': 0xEB, 'd': 0x27, 'e': 0xB2, 'f': 0x75},
    '4': {'0': 0x09, '1': 0x83, '2': 0x2C, '3': 0x1A, '4': 0x1B, '5': 0x6E, '6': 0x5A, '7': 0xA0, '8': 0x52, '9': 0x3B, 'a': 0xD6, 'b': 0xB3, 'c': 0x29, 'd': 0xE3, 'e': 0x2F, 'f': 0x84},
    '5': {'0': 0x53, '1': 0xD1, '2': 0x00, '3': 0xED, '4': 0x20, '5': 0xFC, '6': 0xB1, '7': 0x5B, '8': 0x6A, '9': 0xCB, 'a': 0xBE, 'b': 0x39, 'c': 0x4A, 'd': 0x4C, 'e': 0x58, 'f': 0xCF},
    '6': {'0': 0xD0, '1': 0xEF, '2': 0xAA, '3': 0xFB, '4': 0x43, '5': 0x4D, '6': 0x33, '7': 0x85, '8': 0x45, '9': 0xF9, 'a': 0x02, 'b': 0x7F, 'c': 0x50, 'd': 0x3C, 'e': 0x9F, 'f': 0xA8},
    '7': {'0': 0x51, '1': 0xA3, '2': 0x40, '3': 0x8F, '4': 0x92, '5': 0x9D, '6': 0x38, '7': 0xF5, '8': 0xBC, '9': 0xB6, 'a': 0xDA, 'b': 0x21, 'c': 0x10, 'd': 0xFF, 'e': 0xF3, 'f': 0xD2},
    '8': {'0': 0xCD, '1': 0x0C, '2': 0x13, '3': 0xEC, '4': 0x5F, '5': 0x97, '6': 0x44, '7': 0x17, '8': 0xC4, '9': 0xA7, 'a': 0x7E, 'b': 0x3D, 'c': 0x64, 'd': 0x5D, 'e': 0x19, 'f': 0x73},
    '9': {'0': 0x60, '1': 0x81, '2': 0x4F, '3': 0xDC, '4': 0x22, '5': 0x2A, '6': 0x90, '7': 0x88, '8': 0x46, '9': 0xEE, 'a': 0xB8, 'b': 0x14, 'c': 0xDE, 'd': 0x5E, 'e': 0x0B, 'f': 0xDB},
    'a': {'0': 0xE0, '1': 0x32, '2': 0x3A, '3': 0x0A, '4': 0x49, '5': 0x06, '6': 0x24, '7': 0x5C, '8': 0xC2, '9': 0xD3, 'a': 0xAC, 'b': 0x62, 'c': 0x91, 'd': 0x95, 'e': 0xE4, 'f': 0x79},
    'b': {'0': 0xE7, '1': 0xC8, '2': 0x37, '3': 0x6D, '4': 0x8D, '5': 0xD5, '6': 0x4E, '7': 0xA9, '8': 0x6C, '9': 0x56, 'a': 0xF4, 'b': 0xEA, 'c': 0x65, 'd': 0x7A, 'e': 0xAE, 'f': 0x08},
    'c': {'0': 0xBA, '1': 0x78, '2': 0x25, '3': 0x2E, '4': 0x1C, '5': 0xA6, '6': 0xB4, '7': 0xC6, '8': 0xE8, '9': 0xDD, 'a': 0x74, 'b': 0x1F, 'c': 0x4B, 'd': 0xBD, 'e': 0x8B, 'f': 0x8A},
    'd': {'0': 0x70, '1': 0x3E, '2': 0xB5, '3': 0x66, '4': 0x48, '5': 0x03, '6': 0xF6, '7': 0x0E, '8': 0x61, '9': 0x35, 'a': 0x57, 'b': 0xB9, 'c': 0x86, 'd': 0xC1, 'e': 0x1D, 'f': 0x9E},
    'e': {'0': 0xE1, '1': 0xF8, '2': 0x98, '3': 0x11, '4': 0x69, '5': 0xD9, '6': 0x8E, '7': 0x94, '8': 0x9B, '9': 0x1E, 'a': 0x87, 'b': 0xE9, 'c': 0xCE, 'd': 0x55, 'e': 0x28, 'f': 0xDF},
    'f': {'0': 0x8C, '1': 0xA1, '2': 0x89, '3': 0x0D, '4': 0xBF, '5': 0xE6, '6': 0x42, '7': 0x68, '8': 0x41, '9': 0x99, 'a': 0x2D, 'b': 0x0F, 'c': 0xB0, 'd': 0x54, 'e': 0xBB, 'f': 0x16}
}


s_box_inv = {
    '0': {'0': 0x52, '1': 0x09, '2': 0x6A, '3': 0xD5, '4': 0x30, '5': 0x36, '6': 0xA5, '7': 0x38, '8': 0xBF, '9': 0x40, 'a': 0xA3, 'b': 0x9E, 'c': 0x81, 'd': 0xF3, 'e': 0xD7, 'f': 0xFB},
    '1': {'0': 0x7C, '1': 0xE3, '2': 0x39, '3': 0x82, '4': 0x9B, '5': 0x2F, '6': 0xFF, '7': 0x87, '8': 0x34, '9': 0x8E, 'a': 0x43, 'b': 0x44, 'c': 0xC4, 'd': 0xDE, 'e': 0xE9, 'f': 0xCB},
    '2': {'0': 0x54, '1': 0x7B, '2': 0x94, '3': 0x32, '4': 0xA6, '5': 0xC2, '6': 0x23, '7': 0x3D, '8': 0xEE, '9': 0x4C, 'a': 0x95, 'b': 0x0B, 'c': 0x42, 'd': 0xFA, 'e': 0xC3, 'f': 0x4E},
    '3': {'0': 0x08, '1': 0x2E, '2': 0xA1, '3': 0x66, '4': 0x28, '5': 0xD9, '6': 0x24, '7': 0xB2, '8': 0x76, '9': 0x5B, 'a': 0xA2, 'b': 0x49, 'c': 0x6D, 'd': 0x8B, 'e': 0xD1, 'f': 0x25},
    '4': {'0': 0x72, '1': 0xF8, '2': 0xF6, '3': 0x64, '4': 0x86, '5': 0x68, '6': 0x98, '7': 0x16, '8': 0xD4, '9': 0xA4, 'a': 0x5C, 'b': 0xCC, 'c': 0x5D, 'd': 0x65, 'e': 0xB6, 'f': 0x92},
    '5': {'0': 0x6C, '1': 0x70, '2': 0x48, '3': 0x50, '4': 0xFD, '5': 0xED, '6': 0xB9, '7': 0xDA, '8': 0x5E, '9': 0x15, 'a': 0x46, 'b': 0x57, 'c': 0xA7, 'd': 0x8D, 'e': 0x9D, 'f': 0x84},
    '6': {'0': 0x90, '1': 0xD8, '2': 0xAB, '3': 0x00, '4': 0x8C, '5': 0xBC, '6': 0xD3, '7': 0x0A, '8': 0xF7, '9': 0xE4, 'a': 0x58, 'b': 0x05, 'c': 0xB8, 'd': 0xB3, 'e': 0x45, 'f': 0x06},
    '7': {'0': 0xD0, '1': 0x2C, '2': 0x1E, '3': 0x8F, '4': 0xCA, '5': 0x3F, '6': 0x0F, '7': 0x02, '8': 0xC1, '9': 0xAF, 'a': 0xBD, 'b': 0x03, 'c': 0x01, 'd': 0x13, 'e': 0x8A, 'f': 0x6B},
    '8': {'0': 0x3A, '1': 0x91, '2': 0x11, '3': 0x41, '4': 0x4F, '5': 0x67, '6': 0xDC, '7': 0xEA, '8': 0x97, '9': 0xF2, 'a': 0xCF, 'b': 0xCE, 'c': 0xF0, 'd': 0xB4, 'e': 0xE6, 'f': 0x73},
    '9': {'0': 0x96, '1': 0xAC, '2': 0x74, '3': 0x22, '4': 0xE7, '5': 0xAD, '6': 0x35, '7': 0x85, '8': 0xE2, '9': 0xF9, 'a': 0x37, 'b': 0xE8, 'c': 0x1C, 'd': 0x75, 'e': 0xDF, 'f': 0x6E},
    'a': {'0': 0x47, '1': 0xF1, '2': 0x1A, '3': 0x71, '4': 0x1D, '5': 0x29, '6': 0xC5, '7': 0x89, '8': 0x6F, '9': 0xB7, 'a': 0x62, 'b': 0x0E, 'c': 0xAA, 'd': 0x18, 'e': 0xBE, 'f': 0x1B},
    'b': {'0': 0xFC, '1': 0x56, '2': 0x3E, '3': 0x4B, '4': 0xC6, '5': 0xD2, '6': 0x79, '7': 0x20, '8': 0x9A, '9': 0xDB, 'a': 0xC0, 'b': 0xFE, 'c': 0x78, 'd': 0xCD, 'e': 0x5A, 'f': 0xF4},
    'c': {'0': 0x1F, '1': 0xDD, '2': 0xA8, '3': 0x33, '4': 0x88, '5': 0x07, '6': 0xC7, '7': 0x31, '8': 0xB1, '9': 0x12, 'a': 0x10, 'b': 0x59, 'c': 0x27, 'd': 0x80, 'e': 0xEC, 'f': 0x5F},
    'd': {'0': 0x60, '1': 0x51, '2': 0x7F, '3': 0xA9, '4': 0x19, '5': 0xB5, '6': 0x4A, '7': 0x0D, '8': 0x2D, '9': 0xE5, 'a': 0x7A, 'b': 0x9F, 'c': 0x93, 'd': 0xC9, 'e': 0x9C, 'f': 0xEF},
    'e': {'0': 0xA0, '1': 0xE0, '2': 0x3B, '3': 0x4D, '4': 0xAE, '5': 0x2A, '6': 0xF5, '7': 0xB0, '8': 0xC8, '9': 0xEB, 'a': 0xBB, 'b': 0x3C, 'c': 0x83, 'd': 0x53, 'e': 0x99, 'f': 0x61},
    'f': {'0': 0x17, '1': 0x2B, '2': 0x04, '3': 0x7E, '4': 0xBA, '5': 0x77, '6': 0xD6, '7': 0x26, '8': 0xE1, '9': 0x69, 'a': 0x14, 'b': 0x63, 'c': 0x55, 'd': 0x21, 'e': 0x0C, 'f': 0x7D}
}


def generate_round_keys(initial_key):
    _round_keys = []

    # first should be ignored
    RC = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

    def g(W, k):
        V = [W[1], W[2], W[3], W[0]]

        V[0] = S(V[0])
        V[1] = S(V[1])
        V[2] = S(V[2])
        V[3] = S(V[3])

        V[0] = V[0] ^ RC[k]
        return V

    def xor(a, b):
        _output = []
        for i in range(len(a)):
            ord_xored = a[i] ^ b[i]
            _output.append(ord_xored)
        return _output

    _round_keys.append(initial_key)
    for i in range(1, 11):
        W0 = _round_keys[i - 1][:4]
        W1 = _round_keys[i - 1][4:8]
        W2 = _round_keys[i - 1][8:12]
        W3 = _round_keys[i - 1][12:]

        W0 = xor(g(W0, i), W0)
        W1 = xor(W0, W1)
        W2 = xor(W1, W2)
        W3 = xor(W2, W3)

        _round_keys.append(W0 + W1 + W2 + W3)

    return _round_keys


def S(_input):
    hex_str = hex(_input)
    if len(hex_str) == 3:
        x = '0'
        y = hex_str[2]
    else:
        x = hex_str[2]
        y = hex_str[3]

    return s_box[x][y]


def S_inv(_input):
    hex_str = hex(_input)
    if len(hex_str) == 3:
        x = '0'
        y = hex_str[2]
    else:
        x = hex_str[2]
        y = hex_str[3]

    return s_box_inv[x][y]


def byte_substitution(m):
    for j in range(4):
        for i in range(4):
            m[i][j] = S(m[i][j])
    return m


def byte_substitution_inv(m):
    for j in range(4):
        for i in range(4):
            m[i][j] = S_inv(m[i][j])
    return m


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)

    return a


def diffusion_inv(m, i):
    def mix_columns_inv(m):
        # see Sec 4.1.3 in The Design of Rijndael
        for j in range(4):
            u = xtime(xtime(m[0][j] ^ m[2][j]))
            v = xtime(xtime(m[1][j] ^ m[3][j]))
            m[0][j] ^= u
            m[1][j] ^= v
            m[2][j] ^= u
            m[3][j] ^= v

        for j in range(4):
            a = mix_single_column([m[0][j], m[1][j], m[2][j], m[3][j]])
            m[0][j] = a[0]
            m[1][j] = a[1]
            m[2][j] = a[2]
            m[3][j] = a[3]

        return m

    def shift_rows_inv(m):
        m[1][0], m[1][1], m[1][2], m[1][3] = m[1][3], m[1][0], m[1][1], m[1][2]
        m[2][0], m[2][1], m[2][2], m[2][3] = m[2][2], m[2][3], m[2][0], m[2][1]
        m[3][0], m[3][1], m[3][2], m[3][3] = m[3][1], m[3][2], m[3][3], m[3][0]
        return m

    if i != 10:
        m = mix_columns_inv(m)
    m = shift_rows_inv(m)

    return m


def diffusion(m, i):
    def shift_rows(m):
        m[1][0], m[1][1], m[1][2], m[1][3] = m[1][1], m[1][2], m[1][3], m[1][0]
        m[2][0], m[2][1], m[2][2], m[2][3] = m[2][2], m[2][3], m[2][0], m[2][1]
        m[3][0], m[3][1], m[3][2], m[3][3] = m[3][3], m[3][0], m[3][1], m[3][2]
        return m

    def mix_columns(m):
        for j in range(4):
            a = mix_single_column([m[0][j], m[1][j], m[2][j], m[3][j]])
            m[0][j] = a[0]
            m[1][j] = a[1]
            m[2][j] = a[2]
            m[3][j] = a[3]

        return m

    m = shift_rows(m)
    if i != 10:
        m = mix_columns(m)

    return m


def key_addition(m, key):
    k = 0
    for j in range(4):
        for i in range(4):
            m[i][j] = m[i][j] ^ key[k]
            k += 1
    return m


def rounds(m, _round_keys):
    m = key_addition(m, _round_keys[0])

    for i in range(1, 11):
        m = byte_substitution(m)
        m = diffusion(m, i)
        m = key_addition(m, _round_keys[i])

    return m


def rounds_inv(m, _round_keys):
    i = 10
    while i > 0:
        m = key_addition(m, _round_keys[i])
        m = diffusion_inv(m, i)
        m = byte_substitution_inv(m)
        i -= 1

    m = key_addition(m, _round_keys[0])

    return m


def prepare_data():
    def to_matrix(_list):
        m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        m[0][0] = _list[0]
        m[0][1] = _list[4]
        m[0][2] = _list[8]
        m[0][3] = _list[12]

        m[1][0] = _list[1]
        m[1][1] = _list[5]
        m[1][2] = _list[9]
        m[1][3] = _list[13]

        m[2][0] = _list[2]
        m[2][1] = _list[6]
        m[2][2] = _list[10]
        m[2][3] = _list[14]

        m[3][0] = _list[3]
        m[3][1] = _list[7]
        m[3][2] = _list[11]
        m[3][3] = _list[15]
        return m

    def to_int_list(data_str):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for k in range(0, 16):
            r[k] = ord(data_str[k])
        return r

    key_char_list = sys.argv[1]
    data_char_list = sys.argv[2]

    data_int_list = to_int_list(data_char_list)
    key_int_list = to_int_list(key_char_list)

    m = to_matrix(data_int_list)

    round_keys = generate_round_keys(key_int_list)

    return m, round_keys


def matrix_to_list(m):
    _list = []
    for j in range(4):
        for i in range(4):
            _list.append(m[i][j])
    return _list


def int_list_to_string(_list):
    _str = ''
    for i in range(16):
        _str += chr(_list[i])
    return _str


data_matrix, round_keys = prepare_data()
print(int_list_to_string(matrix_to_list(data_matrix)))

data_matrix = rounds(data_matrix, round_keys)
print(int_list_to_string(matrix_to_list(data_matrix)))

data_matrix = rounds_inv(data_matrix, round_keys)
print(int_list_to_string(matrix_to_list(data_matrix)))
