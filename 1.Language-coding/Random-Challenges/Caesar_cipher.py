s = "abc"


def encrypt(s, n):
    print(ord('a'))
    print(ord('z'))
    result = []
    for c in s:
        if c != ' ':
            # print("char" , c)
            shifted_char_ascii = ord(c) + n
            print(chr(shifted_char_ascii))
            print(shifted_char_ascii)
            if shifted_char_ascii > 122:
                # shifted_char_ascii = 97 + (shifted_char_ascii - 97) % 26
                shifted_char_ascii = 96 + (shifted_char_ascii - 122)
                # print("shifted_char_ascii >> " + str(shifted_char_ascii))
            result.append(chr(shifted_char_ascii))

    result_str = "".join(result)
    print(f"after encrypt {result_str}")
    return result_str


encrypted_str = encrypt(s, 4)


def decript(s: str, n: int):
    result = []
    for c in s:
        print(ord(c))
        shifted_char_ascii = ord(c) - n
        if shifted_char_ascii < 97:
            shifted_char_ascii += 26

        result.append(chr(shifted_char_ascii))

    result_str = "".join(result)
    print(f"after decrypt {result_str}")

decript(encrypted_str,4)
