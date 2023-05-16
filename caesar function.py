'''def encrypt(text, shift):
   new_alphabet = ""
   for letter in text:
       position = alphabet.index(letter)
       new_position = position + shift
       new_letter = alphabet[new_position]
       new_alphabet += new_letter
   print(f"encode text is {new_alphabet}")
def decrypt(text, shift):
    decrypted_alphabet = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decrypted_alphabet += new_letter
    print(f"decode text is {decrypted_alphabet}")
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)'''
