import string
import secrets
# --------------KEY GENERATION------------------------
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