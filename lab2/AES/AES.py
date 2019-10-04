# import sys

key = None
data = None

s_box = {
    '0': {'0': 0x63, '1': 0x7C, '2': 0x77, '3': 0x7B, '4': 0xF2, '5': 0x6B, '6': 0x6F, '7': 0xC5, '8': 0x30, '9': 0x01,
          'a': 0x67, 'b': 0x2B, 'c': 0xFE, 'd': 0xD7, 'e': 0xAB, 'f': 0x76},
    '1': {'0': 0xCA, '1': 0x82, '2': 0xC9, '3': 0x7D, '4': 0xFA, '5': 0x59, '6': 0x47, '7': 0xF0, '8': 0xAD, '9': 0xD4,
          'a': 0xA2, 'b': 0xAF, 'c': 0x9C, 'd': 0xA4, 'e': 0x72, 'f': 0xC0},
    '2': {'0': 0xB7, '1': 0xFD, '2': 0x93, '3': 0x26, '4': 0x36, '5': 0x3F, '6': 0xF7, '7': 0xCC, '8': 0x34, '9': 0xA5,
          'a': 0xE5, 'b': 0xF1, 'c': 0x71, 'd': 0xD8, 'e': 0x31, 'f': 0x15},
    '3': {'0': 0x04, '1': 0xC7, '2': 0x23, '3': 0xC3, '4': 0x18, '5': 0x96, '6': 0x05, '7': 0x9A, '8': 0x07, '9': 0x12,
          'a': 0x80, 'b': 0xE2, 'c': 0xEB, 'd': 0x27, 'e': 0xB2, 'f': 0x75},
    '4': {'0': 0x09, '1': 0x83, '2': 0x2C, '3': 0x1A, '4': 0x1B, '5': 0x6E, '6': 0x5A, '7': 0xA0, '8': 0x52, '9': 0x3B,
          'a': 0xD6, 'b': 0xB3, 'c': 0x29, 'd': 0xE3, 'e': 0x2F, 'f': 0x84},
    '5': {'0': 0x53, '1': 0xD1, '2': 0x00, '3': 0xED, '4': 0x20, '5': 0xFC, '6': 0xB1, '7': 0x5B, '8': 0x6A, '9': 0xCB,
          'a': 0xBE, 'b': 0x39, 'c': 0x4A, 'd': 0x4C, 'e': 0x58, 'f': 0xCF},
    '6': {'0': 0xD0, '1': 0xEF, '2': 0xAA, '3': 0xFB, '4': 0x43, '5': 0x4D, '6': 0x33, '7': 0x85, '8': 0x45, '9': 0xF9,
          'a': 0x02, 'b': 0x7F, 'c': 0x50, 'd': 0x3C, 'e': 0x9F, 'f': 0xA8},
    '7': {'0': 0x51, '1': 0xA3, '2': 0x40, '3': 0x8F, '4': 0x92, '5': 0x9D, '6': 0x38, '7': 0xF5, '8': 0xBC, '9': 0xB6,
          'a': 0xDA, 'b': 0x21, 'c': 0x10, 'd': 0xFF, 'e': 0xF3, 'f': 0xD2},
    '8': {'0': 0xCD, '1': 0x0C, '2': 0x13, '3': 0xEC, '4': 0x5F, '5': 0x97, '6': 0x44, '7': 0x17, '8': 0xC4, '9': 0xA7,
          'a': 0x7E, 'b': 0x3D, 'c': 0x64, 'd': 0x5D, 'e': 0x19, 'f': 0x73},
    '9': {'0': 0x60, '1': 0x81, '2': 0x4F, '3': 0xDC, '4': 0x22, '5': 0x2A, '6': 0x90, '7': 0x88, '8': 0x46, '9': 0xEE,
          'a': 0xB8, 'b': 0x14, 'c': 0xDE, 'd': 0x5E, 'e': 0x0B, 'f': 0xDB},
    'a': {'0': 0xE0, '1': 0x32, '2': 0x3A, '3': 0x0A, '4': 0x49, '5': 0x06, '6': 0x24, '7': 0x5C, '8': 0xC2, '9': 0xD3,
          'a': 0xAC, 'b': 0x62, 'c': 0x91, 'd': 0x95, 'e': 0xE4, 'f': 0x79},
    'b': {'0': 0xE7, '1': 0xC8, '2': 0x37, '3': 0x6D, '4': 0x8D, '5': 0xD5, '6': 0x4E, '7': 0xA9, '8': 0x6C, '9': 0x56,
          'a': 0xF4, 'b': 0xEA, 'c': 0x65, 'd': 0x7A, 'e': 0xAE, 'f': 0x08},
    'c': {'0': 0xBA, '1': 0x78, '2': 0x25, '3': 0x2E, '4': 0x1C, '5': 0xA6, '6': 0xB4, '7': 0xC6, '8': 0xE8, '9': 0xDD,
          'a': 0x74, 'b': 0x1F, 'c': 0x4B, 'd': 0xBD, 'e': 0x8B, 'f': 0x8A},
    'd': {'0': 0x70, '1': 0x3E, '2': 0xB5, '3': 0x66, '4': 0x48, '5': 0x03, '6': 0xF6, '7': 0x0E, '8': 0x61, '9': 0x35,
          'a': 0x57, 'b': 0xB9, 'c': 0x86, 'd': 0xC1, 'e': 0x1D, 'f': 0x9E},
    'e': {'0': 0xE1, '1': 0xF8, '2': 0x98, '3': 0x11, '4': 0x69, '5': 0xD9, '6': 0x8E, '7': 0x94, '8': 0x9B, '9': 0x1E,
          'a': 0x87, 'b': 0xE9, 'c': 0xCE, 'd': 0x55, 'e': 0x28, 'f': 0xDF},
    'f': {'0': 0x8C, '1': 0xA1, '2': 0x89, '3': 0x0D, '4': 0xBF, '5': 0xE6, '6': 0x42, '7': 0x68, '8': 0x41, '9': 0x99,
          'a': 0x2D, 'b': 0x0F, 'c': 0xB0, 'd': 0x54, 'e': 0xBB, 'f': 0x16}
}

# first should be ignored
RC = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
round_keys = []


def S(_input):
    hex_str = hex(_input)
    if len(hex_str) == 3:
        x = '0'
        y = hex_str[2]
    else:
        x = hex_str[2]
        y = hex_str[3]

    return s_box[x][y]


def xor(a, b):
    _output = []
    for i in range(len(a)):
        ord_xored = a[i] ^ b[i]
        _output.append(ord_xored)
    return _output


def generate_round_keys(initial_key):
    def g(W, k):
        V = [W[1], W[2], W[3], W[0]]

        V[0] = S(V[0])
        V[1] = S(V[1])
        V[2] = S(V[2])
        V[3] = S(V[3])

        V[0] = V[0] ^ RC[k]
        return V

    round_keys[0] = initial_key
    for i in range(1, 11):
        W0 = round_keys[i - 1][:4]
        W1 = round_keys[i - 1][4:8]
        W2 = round_keys[i - 1][8:12]
        W3 = round_keys[i - 1][12:]

        W0 = xor(g(W0, i), W0)
        W1 = xor(W0, W1)
        W2 = xor(W1, W2)
        W3 = xor(W2, W3)

        round_keys[i] = W0 + W1 + W2 + W3


def byte_substitution(_data):
    for i in range(len(_data)):
        _data[i] = S(_data[i])
    return _data


def shift_rows(_data):
    s = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # to matrix
    s[0] = (_data[0]), s[0] = (_data[4]), s[0] = (_data[8]), s[0] = (_data[12])
    s[1] = (_data[1]), s[1] = (_data[5]), s[1] = (_data[9]), s[1] = (_data[13])
    s[2] = (_data[2]), s[2] = (_data[6]), s[2] = (_data[10]), s[2] = (_data[14])
    s[3] = (_data[3]), s[3] = (_data[7]), s[3] = (_data[11]), s[3] = (_data[15])

    # shift rows
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

    # to list
    

    return _data


def mix_column(_data):
    return _data


def key_addition(_data):
    return _data


def rounds(_data, _round_keys):
    _data = byte_substitution(_data)

    for i in range(1, 11):
        _data = byte_substitution(_data)
        _data = shift_rows(_data)
        if i < 10:
            _data = mix_column(_data)
        _data = key_addition(_data)

    return _data


def prepare_data():
    global key, data
    # key = list(sys.argv[2])
    # data = list(sys.argv[1])
    key = list('asdfghjklmnbvcxd')
    data = list('asdfghjklmnbvcxd')

    for k in range(0, 16):
        key[k] = ord(key[k])
        data[k] = ord(data[k])


prepare_data()
generate_round_keys(key)
data = rounds(data, round_keys)
print(data)
