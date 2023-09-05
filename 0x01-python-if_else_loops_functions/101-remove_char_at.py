#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        return str[:n] + str[n+1:]
    else:
        return str

# an alternative method:
# def remove_char_at(str, n):
#    new_str = ""
#    for i in range(len(str)):
#        if i != n:
#            new_str = new_str + str[i]
#    return new_str
