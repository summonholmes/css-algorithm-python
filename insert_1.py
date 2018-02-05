def insert_1(bin_arr):
    # Insert a bit of value 1 into the least significant position.
    char_arr = list(bin_arr)
    char_arr.insert(0, '1')
    key = ''.join(char_arr)
    return key
