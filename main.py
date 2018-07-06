from re import sub
from lfsr import lfsr
from full_adder import full_adder
from convert_bin import convert_bin

# Initialize the plaintext
plaintext = ("OnemansmagicisanothermansengineeringSupernaturalisanullword"
             "OnemanstheologyisanothermansbellylaughProgressisntmadebyearly"
             "risersItsmadebylazymentryingtofindeasierwaystodosomething")
plaintext = sub(r'[^\w\s]', '', (''.join(plaintext.split())))  # Letters only
plaintext_bin_arr = [bin(ord(i)).replace('b', '')
                     for i in plaintext]  # Binary list

# Initialize keys - key must be exactly 40 bits
keyword = "Shane"
key = bin(int.from_bytes(keyword.encode(), "big")).replace('b', '')
key_17 = '1' + key[:16]
key_25 = '1' + key[16:]

# Initialize plaintext LFSRs
lfsr_17 = lfsr(key_17, [17, 3], plaintext_bin_arr)
lfsr_25 = lfsr(key_25, [25, 8, 6, 2], plaintext_bin_arr)

# Encrypt
crypt_bin = full_adder(plaintext_bin_arr, lfsr_17, lfsr_25)

# Normalize
for i in range(len(crypt_bin)):
    crypt_bin[i] = str(crypt_bin[i])
crypt_bin_str = "".join(crypt_bin)
crypt_bin_arr = [
    crypt_bin_str[start:start + 8] for start in range(0, len(crypt_bin_str), 8)
]

# Initialize ciphertext LFSRs
lfsr_17 = lfsr(key_17, [17, 3], crypt_bin_arr)
lfsr_25 = lfsr(key_25, [25, 8, 6, 2], crypt_bin_arr)

# Decrypt
decrypt_bin = full_adder(crypt_bin_arr, lfsr_17, lfsr_25)

# Normalize
for i in range(len(decrypt_bin)):
    decrypt_bin[i] = str(decrypt_bin[i])
decrypt_bin_str = "".join(decrypt_bin)
decrypt_bin_arr = [
    decrypt_bin_str[start:start + 8]
    for start in range(0, len(decrypt_bin_str), 8)
]

# Print the results
print("The keyword: ", keyword)
print("The plaintext: ", convert_bin(plaintext_bin_arr)[0:75])
print("The ciphertext: ", convert_bin(crypt_bin_arr))
print("The dectext: ", convert_bin(decrypt_bin_arr)[0:75])
