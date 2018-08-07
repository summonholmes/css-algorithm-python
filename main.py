def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    # Thanks jfs - convert-binary-to-ascii-and-vice-versa
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='ignore'):
    # Thanks jfs - convert-binary-to-ascii-and-vice-versa
    n = int(bits, 2)
    return n.to_bytes(
        (n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def LFSR(text_bin, key, poly, xor, lfsr):
    # The lfsr is generated by the key and polynomial
    for char in text_bin:
        xor = sum(int(key[num]) for num in poly)
        xor = 0 if xor % 2 == 0 else 1
        lfsr.append(xor)
        key = str(xor) + key[:-1]
        xor = 0
    return lfsr


def FullAdder(text_bin, lfsr_17, lfsr_25, cin, crypt_bin):
    # This is the standard full-adder truth table
    for i, char in enumerate(text_bin):
        if lfsr_17[i] + lfsr_25[i] + cin == 0:
            s = 0
            cout = 0
        elif lfsr_17[i] + lfsr_25[i] + cin == 1:
            s = 1
            cout = 0
        elif lfsr_17[i] + lfsr_25[i] + cin == 2:
            s = 0
            cout = 1
        elif lfsr_17[i] + lfsr_25[i] + cin == 3:
            s = 1
            cout = 1
        cin = cout
        crypt_bin.append((s + int(char)) % 2)
    return crypt_bin


### Plaintext
plaintext = ("OnemansmagicisanothermansengineeringSupernaturalisanullword"
             "OnemanstheologyisanothermansbellylaughProgressisntmadebyearly"
             "risersItsmadebylazymentryingtofindeasierwaystodosomething")
plaintext_bin = text_to_bits(plaintext)

### Keyword
keyword = "Shane"
keyword_bin = text_to_bits(keyword)

### Keys
key_17 = '1' + keyword_bin[:16]
key_25 = '1' + keyword_bin[16:]

### LFSR Plaintext
lfsr_17 = LFSR(plaintext_bin, key_17, [16, 2], 0, [])
lfsr_25 = LFSR(plaintext_bin, key_25, [24, 7, 5, 1], 0, [])

### Full Adder Plaintext
ciphertext_bin = FullAdder(plaintext_bin, lfsr_17, lfsr_25, 0, [])

### Output Ciphertext
ciphertext_bin = ''.join(map(str, ciphertext_bin))
ciphertext = text_from_bits(ciphertext_bin)

### LFSR 17 Ciphertext
lfsr_17 = LFSR(ciphertext_bin, key_17, [16, 2], 0, [])
lfsr_25 = LFSR(ciphertext_bin, key_25, [24, 7, 5, 1], 0, [])

### Full Adder Ciphertext
dectext_bin = FullAdder(ciphertext_bin, lfsr_17, lfsr_25, 0, [])

### Output Dectext
dectext_bin = "".join(map(str, dectext_bin))
dectext = text_from_bits(dectext_bin)

### Print the results
print("The keyword: ", keyword)
print("The plaintext: ", plaintext[0:75])
print("The ciphertext: ", ciphertext[0:75])
print("The dectext: ", dectext[0:75])