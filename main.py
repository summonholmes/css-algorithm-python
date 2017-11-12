#!/usr/bin/env python
from insert_1 import insert_1
from full_adder import full_adder
import convert


def main():
	# Initialize the keyword and plaintext as strings.
	keyword = "Shane"
	key_arr = list(keyword)
	key_bin_arr = []
	# plaintext = "ThisProjectMakesMeWantToPullMyHairOut"
	plaintext = "OnemansmagicisanothermansengineeringSupernaturalisanullwordOnemanstheologyisanothermansbellylaughProgressisntmadebyearlyrisersItsmadebylazymentryingtofindeasierwaystodosomething"
	plaintext_arr = list(plaintext)
	plaintext_bin_arr = []

	# Perform string to binary conversion for the keyword and plaintext.
	for i in range(len(key_arr)):
		key_bin_arr.append(bin(ord(key_arr[i])))
		key_bin_arr[i] = key_bin_arr[i].replace("b", "")
	for j in range(len(plaintext_arr)):
		plaintext_bin_arr.append(bin(ord(plaintext_arr[j])))
		plaintext_bin_arr[j] = plaintext_bin_arr[j].replace("b", "")

	# Perform the full encryption/decryption routine.
	key_17 = insert_1(key_bin_arr[0] + key_bin_arr[1])
	key_25 = insert_1(key_bin_arr[2] + key_bin_arr[3] + key_bin_arr[4])
	ciphertext_bin_arr = full_adder(key_17, key_25, plaintext_bin_arr)
	decrypt_text_bin_arr = full_adder(key_17, key_25, ciphertext_bin_arr)

	# Print the final results.  Output is formatted to demonstrate that the binary conversion process works.
	print("\nThe keyword: ", keyword)
	print("The plaintext: ", convert.convert_key_bin_arr(plaintext_bin_arr))
	print("The ciphertext: ", convert.convert_enc_key(ciphertext_bin_arr))
	print("The decrypted ciphertext: ", convert.convert_dec_key(decrypt_text_bin_arr))
	print("Plaintext binary array: ", plaintext_bin_arr)
	print("Ciphertext binary array: ", ciphertext_bin_arr)
	print("Decrypted ciphertext binary array: ", decrypt_text_bin_arr)
	input("\nPress enter to exit")

	return 0

main()
