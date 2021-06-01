from caesar_cipher import __version__
from caesar_cipher.cipher import encrypt, decrypt, crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    """encrypt a string with a given shift
    encryption should handle upper and lower case letters
    encryption should allow non-alpha characters but ignore them, including white space
    """
    actual = encrypt('i Did not find it, please go back!',5)
    expected = 'n ini sty knsi ny uqjfxj lt gfhp'
    assert actual == expected

def test_decrypt():
    """decrypt a previously encrypted string with the same shift
    """
    actual = decrypt('n ini sty knsi ny uqjfxj lt gfhp',5)
    expected = 'i did not find it please go back'
    assert actual == expected    

def test_crack():
    """decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used."""
    actual = crack('n ini sty knsi ny uqjfxj lt gfhp')
    expected = 'i did not find it please go back'
    assert actual == expected      


