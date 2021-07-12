

s = "abcd xyz"

def encrypt(s , n):
    print(ord('a'))
    print(ord('z'))
    result = []
    for c in s:
        if c != ' ':
            #print("char" , c)
            shifted_char_ascii = ord(c) + n
            if shifted_char_ascii > 122:
                #shifted_char_ascii = 97 + (shifted_char_ascii - 97) % 26
                shifted_char_ascii = shifted_char_ascii - 122
                #print("shifted_char_ascii >> " + str(shifted_char_ascii))
            result.append( chr(shifted_char_ascii) )

    result_str = "".join(result)
    print(result_str)



encrypt(s, 4)


# def decrypt(s , n):
#     result = []
#     for c in s:
#         print("char " , c)
#         shifted_char_ascii = ord(c) - n
#         if shifted_char_ascii < 97:
#             shifted_char_ascii = 97shifted_char_ascii + 26
