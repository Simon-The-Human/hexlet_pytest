def reverse(string):
    rev =  str(string)[::-1]
    if type(string) == int:
        return int(rev)
    return rev