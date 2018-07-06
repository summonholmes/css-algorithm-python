def convert_bin(bin_arr):
    # Binary array to string
    str_text = ''.join(str(i) for i in bin_arr)
    text = ''.join(
        chr(int(str_text[i:i + 8], 2)) for i in range(0, len(str_text), 8))
    return text
