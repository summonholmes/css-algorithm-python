#!/usr/bin/env python
from insert_1 import insert_1
from full_adder import full_adder
import convert


def main():
    # Initialize the keyword and plaintext as strings.
    # Perform string to binary conversion for the keyword and plaintext.
    keyword = "Shane"
    key_bin_arr = [(bin(ord(list(keyword)[i]))).replace("b", "")
                   for i in range(len(list(keyword)))]
    plaintext = (
        'OnemansmagicisanothermansengineeringSupernaturalisanullword'
        'OnemanstheologyisanothermansbellylaughProgressisntmadebyearly'
        'risersItsmadebylazymentryingtofindeasierwaystodosomething')
    plaintext_bin_arr = [(bin(ord(list(plaintext)[i]))).replace("b", "")
                         for i in range(len(list(plaintext)))]

    # Perform the full encryption/decryption routine.
    key_17 = insert_1(key_bin_arr[0] + key_bin_arr[1])
    key_25 = insert_1(key_bin_arr[2] + key_bin_arr[3] + key_bin_arr[4])
    ciphertext_bin_arr = full_adder(key_17, key_25, plaintext_bin_arr)
    decrypt_text_bin_arr = full_adder(key_17, key_25, ciphertext_bin_arr)

    # Print the final results.  Output is formatted to demonstrate that the
    # binary conversion process works.
    print("\nThe keyword: ", keyword)
    print("The plaintext: ",
          convert.convert_key_bin_arr(plaintext_bin_arr)[0:75])
    print("The ciphertext: ",
          convert.convert_enc_key(ciphertext_bin_arr)[0:75])
    print("The decrypted ciphertext: ",
          convert.convert_dec_key(decrypt_text_bin_arr)[0:75])

main()
