from lfsr import lfsr
from bit_truth import bit_truth


def full_adder(key_17, key_25, bin_arr):
    # Get the lsfr outputs, group by 8 elements, then perform full adder in
    # bit_truth.py.
    lfsr_17 = lfsr(key_17,  [17, 3], bin_arr)
    lfsr_25 = lfsr(key_25, [25, 8, 6, 2], bin_arr)
    split_lfsr_17 = [lfsr_17[start:start + 8]
                     for start in range(0, len(lfsr_17), 8)]
    split_lfsr_25 = [lfsr_25[start:start + 8]
                     for start in range(0, len(lfsr_25), 8)]

    # Retrieve the plaintext-lfsr bit xor output from the truth table.
    crypt_bin = bit_truth(bin_arr, split_lfsr_17, split_lfsr_25)

    # Convert the binary data to strings of 8 characters (So the process can
    # repeat itself).
    for i in range(len(crypt_bin)):
        crypt_bin[i] = str(crypt_bin[i])
    crypt_bin_str = "".join(crypt_bin)
    crypt_bin_arr = [crypt_bin_str[start:start + 8]
                     for start in range(0, len(crypt_bin_str), 8)]

    return crypt_bin_arr
