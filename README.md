# css-cryptosystem
The Content Scramble System (CSS) is a cryptosystem that utilizes plaintext, a key of 30 bits, two Linear Feedback Shift Registers (LFSR) of sizes 17 and 25, and Full Adder.  This cryptosystem is interesting because the actual bits that compose the plaintext characters and key are utilized.  One of the most interesting features of this cryptosystem is that the LFSRs don't utilize the actual plaintext characters at all.  Instead, the supplied key and length of the plaintext is utilized.  The plaintext isn't utilized until the Full Adder step, where the appropriate '0' or '1' is added to the current bit and modded by 2.  The process then repeats itself in reverse as is, with no modifications to the ciphertext.

## Dependencies
The only requirement for this implementation is base Python 3.

## Usage
If necessary, edit the plaintext and keyword variables in main.py.  The key must be 5 characters.  When finished, run:
```
$ /path/to/main.py
```

License
===

This project is licensed under the [GNU General Public License GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

