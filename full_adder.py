def full_adder(bin_arr, split_lfsr_17, split_lfsr_25):
    # The full-adder truth table below is utilized to determine the final bit
    # values to be output.
    cin = 0
    cout = 0
    s = []
    crypt_bin = []

    # Using the same looping rules from lfsr.py:
    for i in range(len(bin_arr)):
        for j in range(len(bin_arr[i])):
            if split_lfsr_17[i][j] == 0 and split_lfsr_25[i][j] == 0 and cin == 0:
                s.append(0)
                cout = 0
            elif split_lfsr_17[i][j] == 0 and split_lfsr_25[i][j] == 0 and cin == 1:
                s.append(1)
                cout = 0
            elif split_lfsr_17[i][j] == 0 and split_lfsr_25[i][j] == 1 and cin == 0:
                s.append(1)
                cout = 0
            elif split_lfsr_17[i][j] == 0 and split_lfsr_25[i][j] == 1 and cin == 1:
                s.append(0)
                cout = 1
            elif split_lfsr_17[i][j] == 1 and split_lfsr_25[i][j] == 0 and cin == 0:
                s.append(1)
                cout = 0
            elif split_lfsr_17[i][j] == 1 and split_lfsr_25[i][j] == 0 and cin == 1:
                s.append(0)
                cout = 1
            elif split_lfsr_17[i][j] == 1 and split_lfsr_25[i][j] == 1 and cin == 0:
                s.append(0)
                cout = 1
            elif split_lfsr_17[i][j] == 1 and split_lfsr_25[i][j] == 1 and cin == 1:
                s.append(1)
                cout = 1
            else:
                print("An error occured.  Now exiting")
                exit(0)
            cin = cout
            # Xor to obtain the bit to append.  Repeat until the loops finish,
            # and return the final result.
            crypt_bin.append((s[i] + int(bin_arr[i][j])) % 2)

    return crypt_bin
