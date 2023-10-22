import classical_keys
import re, os, sys

#---------------------ENCRYPTION SCHEME------------------------------------
# This function simulates what is known as Shift Cipher. Although,
# various variations exist, Caeser's cipher is a variation encrypted by moving
# each letter in the plaintext with the 3rd letter away from it in the alphabet.
# Rot-13 is another variation that shifts letter by 13 spaces
# Shift cipher uses a shift value with key in the range [0,25].
# In this implementation, we replace characters not in the alphabets with
#  numbers and the ciphertext are all in uppercase
def sencrypt(filename:str, key:int) -> str:
    # This is because we will be providing an implementation where we can run this function from CLI and CLI is passed as strings i.e. sys.argv
    if (type(key) != int):
        key = int(key)

    cipher_text = []
    output = ''
    
    # This function encrypts each character of a string, by moving it 'shifts' # pos forward. It takes each alphabets and moves it. if an alphabet is at
    # the end, it wraps around
    def helper_encrypt(char):
        cipher = ''
        alphabets = classical_keys.keys.get('alpha')
        special = classical_keys.keys.get('special')

        if char not in special and  char.lower() in alphabets:
            index = alphabets.index(char.lower())
            cipher_index = (index + key) % 26
            cipher = alphabets[cipher_index].upper()      
        else:
            cipher = special[char]
                        
        return cipher
    
    # Here, we read each character from file and encrypt
    with open(filename, 'r') as file:
        while True:
            char = file.read(1)
            
            # EOF
            if not char:
                break
            else:
                cipher_text.append(helper_encrypt(char))
 

    # Breaking ciphertext into a chunk of 6. This is not necessary.
    chunks = [''.join(cipher_text[i:i+6]) for i in range(0, len(cipher_text), 6)]
    cipher_text = ' '.join(chunks)
    
    # Determining what encrypted file name should be
    if key == 13:
        output = 'rot13_'+filename
    elif key == 3:
        output = 'caesar_'+filename
    else:
        output = 'sub_'+filename
        
    
    # Here, we store our ciphertext into a file with the name output
    with open(output, 'w') as file:
        file.write(cipher_text)
    

    return output

#------------------------DECRYPTION SCHEME-------------------------------
# This function represents the decryption process for the implementation of shift cipher. Here, we basically walk back what we do for encrypting using the shift cipher.
def sdecrypt(cipherfile:str, key:int)->str:
    # This is because we will be providing an implementation where we can run this function from CLI and CLI is passed as strings i.e. sys.argv
    if (type(key) != int):
        key = int(key)
    
    if (os.path.exists(cipherfile)) and (os.path.getsize(cipherfile) > 0):
        plaintext = []

        # This function decrypts a single character by moving it key positions 
        # backwards and wrapping around as needed
        def helper_decrypt(char):
            plain = ''
            alphabets = classical_keys.keys.get('alpha')
            special = classical_keys.keys.get('special')

            if char.lower() in alphabets:
                index = alphabets.index(char.lower())
                plain = alphabets[(index - key) % 26]
            else:
                plain = ''.join([key for key in special if special[key] == char])

            return plain
        
        # Since we used a spacing of 6, first we read the entire file into a list. 
        # We will do this line by line, and store each line as a list
        # and then join to remove the spacing of 6
        with open(cipherfile, 'r') as file:
            for line in file:
                line = line.replace(' ','') # remove all whitespace on line
                decrypted_line = []

                # iterating through each string on the line and decrypting
                for indx, char in enumerate(line):
                    # If we find a full stop, we capitalize the word
                    if len(decrypted_line) > 0 and line[indx - 1] == '2':
                        decrypted_line.append((helper_decrypt(char)).upper())
                    else:
                        decrypted_line.append(helper_decrypt(char))

                decrypted_line[0] = decrypted_line[0].upper()
                plaintext.append(decrypted_line) # add it to our plaintext list

        # convert each line to a string
        plaintext = [''.join(lines) for lines in plaintext]
        plaintext = '\n'.join(plaintext)# add line breaks after end of each lne 

        # determing file_name based on patterns in the name of encrypted file
        pattern = ['shift_', 'rot13_', 'caesar_']
        filename = 'dec.txt'

        # Constructing what the decrypted file name should be -TODO
        for sub_str in pattern:
            if re.match(sub_str,cipherfile):
                filename = 'dec_'+cipherfile[len(sub_str):]
            
        
        # open the file and then write to it
        with open(filename, 'w') as file:
            file.write(plaintext)

        return filename
    
    else:
        print('File is either empty or doesnt exist. Please check file for these conditions')

        # putting all our functions into a map to be used by cmd
functions = {
    's_encrypt': sencrypt,
    's_decrypt': sdecrypt,
}

# Making CLI commands
if __name__ == '__main__':
    # gets the second argument in CLI, which should be function name
    function_name = sys.argv[1]
    params = sys.argv[2:]

    # simply use our dictionary to call the function using params. The following simply checks if the function name is actually a function and then calls it
    if function_name in functions.keys():
        # first we get the function from our dictionary, then apply the parameters. Here, we use tuple unpacking
        (functions.get(function_name))(*params)
    else:
        print('Invalid Command. Please refer to read me')