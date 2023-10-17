import string
import sys

alphabets = list(string.ascii_uppercase)

# distance is quite a bad name for this function, but what is done here, is that
# this function takes two letters, a ciphertext and plaintext and attempts to find
# the number of shift from the plaintext letter to ciphertext letter. This is obviously
# applicable only to english language and can be used to quickly decipher simple encryption
# schemes like shift cipher or caesar cipher
def distance(cipher, plain):
    distance = alphabets.index(cipher.upper()) - alphabets.index(plain.upper())

    if distance < 0:
        distance += len(alphabets)

    print(plain, "is", distance,"letter(s) from",cipher)

    return distance

# This function performs a sort of frequency analysis on a given ciphertext and checks the
# number of times each ciphertext character is used. The results are in percentage and
# can be compared to the English language frequency analysis, This is quite useful when trying
# to break a substuition cipher
def frequency_analysis(filename):
    ciphertext = ''

    with open(filename, 'r') as file:
        ciphertext += file.read()
    
    ciphertext = str(ciphertext)
    # Here, we remove whitespace and new line chars from cipher_text and transform to a list
    cipher_list = (ciphertext.replace(" ","")).replace('\n','')
    frequency = [(round((cipher_list.count(x)/len(cipher_list)) * 100, 1)) for x in cipher_list]
    distribution = dict([(letter.upper(), freq) for letter, freq in zip(cipher_list, frequency)])
    print('The values are in percentage: \n', distribution)

    return distribution

# making a dictionary of all available funcions in this file. This will determine how we will call the
# functions from CLI
functions = {
        'distance' : distance,
        'frequency_analysis' : frequency_analysis
}

if __name__ == '__main__':
    function_name = sys.argv[1] # grabs the function name that user is currenly using in CLI
    params = sys.argv[2:] # after the function name, everything else should be a parameter
    
    function_to_use = functions.get(function_name) # we determine the actual function user typed in

    # Observe that here, we did not print the result of calling the function. This is because, in
    # each function itself, we print and echo output before returning.
    if function_to_use:
        function_to_use(*params)
        
