def convert_key_bin_arr(key_bin_arr):
	# Convert the plaintext binary into the plaintext string.
	str_plain = ''.join(str(i) for i in key_bin_arr)
	plaintext = ''.join(chr(int(str_plain[i:i + 8], 2)) for i in range(0, len(str_plain), 8))
	return plaintext


def convert_enc_key(enc_key):
	# Convert the ciphertext binary into the ciphertext string.
	str_enc_key = ''.join(str(i) for i in enc_key)
	ciphertext = ''.join(chr(int(str_enc_key[i:i + 8], 2)) for i in range(0, len(str_enc_key), 8))
	return ciphertext


def convert_dec_key(dec_key):
	# Convert the decrypted ciphertext binary into the decrypted ciphertext string.
	str_dec_key = ''.join(str(i) for i in dec_key)
	dec_text = ''.join(chr(int(str_dec_key[i:i + 8], 2)) for i in range(0, len(str_dec_key), 8))
	return dec_text
