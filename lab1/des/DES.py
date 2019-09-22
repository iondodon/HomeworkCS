IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)

IP_INV = (
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
)

PC1 = (
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
)

PC2 = (
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)

E = (
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)

P = (
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
)

Sboxes = {
    0: (
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ),
    1: (
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ),
    2: (
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ),
    3: (
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ),
    4: (
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ),
    5: (
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ),
    6: (
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ),
    7: (
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    )
}


def text_to_bin(text):
    bin_str = ''
    for ch in text:
        ord_ch = ord(ch)
        c = ''
        while ord_ch > 0:
            c = str(ord_ch % 2) + c
            ord_ch //= 2
        while len(c) < 8:
            c = '0' + c
        bin_str += c
    return bin_str


def to_bin(a):
    """gets int, returns 4 bits string as each sbox should do"""
    c = ''
    while a > 0:
        c = str(a % 2) + c
        a //= 2
    while len(c) < 4:
        c = '0' + c
    return c


def bin_to_text(bin_text):
    text = ''

    i = 0
    while i < 64:
        num = 0
        bin_str = bin_text[i:i + 8]

        if bin_str[7] == '1': num += 1
        if bin_str[6] == '1': num += 2
        if bin_str[5] == '1': num += 4
        if bin_str[4] == '1': num += 8
        if bin_str[3] == '1': num += 16
        if bin_str[2] == '1': num += 32
        if bin_str[1] == '1': num += 64
        if bin_str[0] == '1': num += 128

        text += chr(num)
        i += 8

    return text


def to_int(string_number):
    """returns int"""
    c = 0
    reverse_string_number = ''
    for k in range(len(string_number)):
        reverse_string_number += string_number[len(string_number) - k - 1]

    for k in range(len(reverse_string_number)):
        if reverse_string_number[k] == '1':
            c += 2 ** k
    return c


def xor(a, b):
    """xor bit operation"""
    c = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            c += '1'
        else:
            c += '0'
    return c


def permute_by_table(input_bin, table):
    output_bin = ''
    for i in range(len(table)):
        output_bin += input_bin[table[i] - 1]

    return output_bin


def sboxes_perform(sbinput):
    sboutput = ''
    for j in range(8):
        start = j * 6
        box_in = sbinput[start:start + 6]
        raw = to_int(box_in[0] + box_in[5])
        col = to_int(box_in[1:5])
        num = Sboxes[j][16 * (raw - 1) + (col - 1)]
        sboutput += to_bin(num)
    return sboutput


def generate_round_keys(initial_key):
    lrot_values = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

    round_keys = []

    prev_key = permute_by_table(initial_key, PC1)
    for k in range(16):
        new_key = prev_key
        for i in range(lrot_values[k]):
            key_left = new_key[:28]
            key_right = new_key[28:]

            key_left += key_left[0]
            key_left = key_left[1:]
            key_right += key_right[0]
            key_right = key_right[1:]

            new_key = key_left + key_right

        prev_key = new_key
        round_keys.append(permute_by_table(new_key, PC2))
    return round_keys


def f_function(R, round_key):
    str_bin = permute_by_table(R, E)
    str_bin = xor(str_bin, round_key)

    str_bin = sboxes_perform(str_bin)
    str_bin = permute_by_table(str_bin, P)

    return str_bin


def round_cycles(text_bin, round_keys, method):
    # initial permutation
    text_bin = permute_by_table(text_bin, IP)

    L = text_bin[:32]
    R = text_bin[32:]
    for i in range(16):
        if method == 0:
            round_key = round_keys[i]
        else:
            round_key = round_keys[16 - i - 1]
        L_new = R
        R_new = xor(L, f_function(R, round_key))
        L = L_new
        R = R_new

    # final permutation
    output_bin = permute_by_table(R + L, IP_INV)

    return output_bin


def encrypt(_msg, _key):
    text_bin = text_to_bin(_msg)
    key_bin = text_to_bin(_key)
    round_keys = generate_round_keys(key_bin)
    encrypted_text = round_cycles(text_bin, round_keys, 0)
    return encrypted_text


def decrypt(_encrypted_text, _key):
    text_bin = text_to_bin(_encrypted_text)
    key_bin = text_to_bin(_key)
    round_keys = generate_round_keys(key_bin)
    decrypted_text = round_cycles(text_bin, round_keys, 1)
    return decrypted_text


msg = 'qwertyui'
key = 'qwertyui'

print(bin_to_text(encrypt(msg, key)))
print(bin_to_text(decrypt(msg, key)))
