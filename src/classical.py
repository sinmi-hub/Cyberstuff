import os, re, secrets, sys, string

keys = {
    'alpha' : list(string.ascii_lowercase), # list of alphabets
    'special' : {
        ".": "2",
        ",": "4",
        ":": "6",
        " ": '8',
        '\n': '3',
        '\'': '7',
        '\"': '9',
        '_' : '1',
        '—': '5',
        ';': ';',
        '-': '-',
        '?': '?'
    },
    'vkey': secrets.token_hex(32) # creates a key 64 characters long
}

num_alpha ={
    '0': 'zero',
    '1': 'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5': 'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
}


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
        alphabets = keys.get('alpha')
        special = keys.get('special')

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
        output = 'shift_'+filename
        
    
    # Here, we store our ciphertext into a file with the name output
    with open(output, 'w') as file:
        file.write(cipher_text)
    

    return output

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
            alphabets = keys.get('alpha')
            special = keys.get('special')

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

def vencrypt(filename:str)->str:

    # First we pull the randomly generated key and use it as a token for the scheme
    token = keys.get('vkey')


    return ''
    
def vdecrypt(filename:str) ->str:
    return ''



# putting all our functions into a map to be used by cmd
functions = {
    's_encrypt': sencrypt,
    's_decrypt': sdecrypt,
    'v_encrypt': vencrypt,
    'v_decrypt': vdecrypt
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

# HELPER FUNCTION

# This function pretty much creates a alphabetic representation of a specific #
# key that has digits in it. We will then truncate or add to the key length to #
# fit the cipherfile characters. This function is to be used in the Vignere #
# cipher to generate a keyword to be used.

def gen(token:str, length:int) -> str:
    
    msg_length = length
    # converts every possible digit that might appear in a token to alphabets
    def num_alpha_conv(token:str) -> str:
        new_token = ''.join([num_alpha[x] if x.isdigit() else x for x in token])
        return new_token

    # Here, we construct key length to be the same as the message length
    def constructkey_len(word_token:str) -> str:
        new_token = word_token

        # if it is greater, we want to truncate and return immediately
        if len(new_token) > msg_length:
            new_token = new_token[:msg_length]
            return new_token

        elif len(new_token) < msg_length:
            # generate a 4 and 8 character long subkey and convert digit in it
            subky_strt = num_alpha_conv(secrets.token_hex(4))
            subky_stp = num_alpha_conv(secrets.token_hex(2))
            start = step = 0

            # we iterate through the characters in the subkey and add their #
            # position in the alphabets together. Notice, we use one indexing #
            # here, and nor zero
            for indx,_ in enumerate(subky_strt):
                start += (((keys.get('alpha')).index(subky_strt[indx])) + 1)

                if indx < (len(subky_stp)) :
                    step += (((keys.get('alpha')).index(subky_stp[indx])) + 1)
                
                # keeping start and end in valid ranges
                start = (start % len(new_token))
                step = (step % len(new_token))

            # I AM GONNA REGRET THE ZERO READBILITY, BUT OH WELL
            print(start)
            print(step)

            to_append = ''.join([new_token[(start + i + step) % len(new_token)] for i in range(len(new_token))])

            # our new key of length 128
            new_token += to_append
            
            # We will recursively call the function to determine if our new key # is too long or short
            constructkey_len(new_token)
            
        else:
            return new_token
        
    # generating key to use vignere ecnryption scheme
    k = num_alpha_conv(token)
    k = constructkey_len(k)

    return k

















                

# Comments for specific places
# -------------elif case for gen(), sub_func: constructkey_len():---------------
        # else, if it is less than, we want to add to it. We wont simply repeat 
        # the key here, but random parts of the key will be added together, 
        # which will the be appended to the original key. Given that our 
        # current key is len of 64, our aim will be at least 128. We will also 
        # make sure to call recursively, just in case we need a longer length. 
        # This ensures the key length and message length is the same. Here, we #
        # mimic some properties of One Time Pad