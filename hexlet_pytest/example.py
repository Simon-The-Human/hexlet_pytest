def reverse(string):
    rev = str(string)[::-1]
    if isinstance(string, int):
        return int(rev)
    return rev
