# css-cryptosystem
The Content Scramble System (CSS) is a cryptosystem that utilizes plaintext, a key of 30 bits, two Linear Feedback Shift Registers (LFSR) of sizes 17 and 25, and Full Adder.  This cryptosystem is unique because the actual bits that compose the plaintext characters and key are utilized.  One of the most interesting features of this cryptosystem is that the LFSRs don't utilize the actual plaintext characters at all.  Instead, the supplied key and length of the plaintext are iterated over to generate deterministic bits of '0' or '1'.  The plaintext isn't utilized until the Full Adder step, where the appropriate '0' or '1' is added to the current bit and modded by 2.  The process then repeats itself in reverse with no actual modifications to the ciphertext.

## Dependencies
The only requirement for this implementation is base Python 3.

## Usage
If necessary, edit the plaintext and keyword variables in main.py.  Most characters, including punctuation, are acceptable.  The key must be exactly 30 bits or 5 characters.  When finished, run:
```
$ python /path/to/css.py
```

## Example
```
 shanekimble@Shanes-MacBook-Pro  ~  python Documents/Code/Git_summonholmes/css-cryptosystem/css.py 
The keyword:  Shane
The plaintext:  OnemansmagicisanothermansengineeringSupernaturalisanullwordOnemanstheologyi
The ciphertext:  xh`/|\F/rq?O#Wۏ`-OО@*cV
                                         |iSˈ)j	`;/
                                                   3r\͸o;T+CNDt7tGLۨ`}B
The dectext:  OnemansmagicisanothermansengineeringSupernaturalisanullwordOnemanstheologyi

```

License
===

This project is licensed under the [GNU General Public License GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

