import classical_keys
import secrets, sys


keyspace = classical_keys()
# This function pretty much creates a alphabetic representation of a specific
# key that has digits in it. We will then truncate or add to the key length to #
# fit the cipherfile characters. This function is to be used in the Vignere #
# cipher to generate a keyword to be used.
def gen(token:str, length:int) -> str:
    
    msg_length = length
    # converts every possible digit that might appear in a token to alphabets
    def num_alpha_conv(token:str) -> str:
        new_token = ''.join([keyspace.num_alpha[x] if x.isdigit() else x for x in token])
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
                start += (((keyspace.keys.get('alpha')).index(subky_strt[indx])) + 1)

                if indx < (len(subky_stp)) :
                    step += (((keyspace.keys.get('alpha')).index(subky_stp[indx])) + 1)
                
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


def vencrypt(filename:str)->str:

    # First we pull the randomly generated key and use it as a token for the scheme
    token = keyspace.keys.get('vkey')


    return ''
    
def vdecrypt(filename:str) ->str:
    return ''



# putting all our functions into a map to be used by cmd
functions = {
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


















                

# Comments for specific places
# -------------elif case for gen(), sub_func: constructkey_len():---------------
        # else, if it is less than, we want to add to it. We wont simply repeat 
        # the key here, but random parts of the key will be added together, 
        # which will the be appended to the original key. Given that our 
        # current key is len of 64, our aim will be at least 128. We will also 
        # make sure to call recursively, just in case we need a longer length. 
        # This ensures the key length and message length is the same. Here, we #
        # mimic some properties of One Time Pad