This ReadMe file contains information about the structure of this project. 

There is the src directory and the tests directory. In the src directory, the file, "classical.py' contains an implementation of the Shift's cipher, Vignere Cipher, and Polybius Cipher. 

This includes both the encryption and decryption process for each scheme.
The key is also contained in this file.
We can simply encrypt/decrypt straight from the command line by running commands

To use the Shift cipher:
``Encryption: CLI command: python3 class_scheme/shift.py s_encrypt 'file-name' 'key'``
``Decryption: CLI command: python3 class_scheme/shift.py s_decrypt 'file-name' 'key'``

To use the Vignere cipher:
Encryption: CLI command: python3 class_scheme/classical.py v_encrypt 'file - name' 'key'
Decryption: CLI command: python3 class_scheme/classical.py v_decrypt 'file-name' 'key'

To use the Polybius cipher
Encryption: CLI command: python3 class_scheme/classical.py v_encrypt 'file - name' 'key'
Decryption: CLI command: python3 class_scheme/classical.py v_decrypt 'file-name' 'key'

 
## OTHER TOOLS
In 'toolbox/encryption_tools.py', there are two functions. Each of this function can be run straight from the CLI by providing the function name and
parameter. distance is of the following structure: 

distance(ciphertext_char, plaintext_char)
CLI command: python3 encryption_tools.py distance 'ciphertext_char' 'plaintext_char'
``Distance: This is used as a possible tool for shift ciphers. It takes two parameters: a plain text character and a ciphertext character and it finds the number of letters that the plaintext character has been shifted or rotated by. This is a useful tool when trying to determine the key for a shift-based cipher.``

frequency_analysis(ciphertext)
CLI command: python3 encryption_tools.py frequency_analysis 'ciphertext'
``Frequency_analysis: This tool simply takes a ciphertext and constructs a frequency analysis of each ciphertext character. This is useful when trying to determine how to break a substitution cipher. This can be used in tandem with other tools to figure out a key that is based on mapping or any other things.``

Keylogger - In progress
