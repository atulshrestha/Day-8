alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
#message = input("enter message to be encrypted: \n").lower()
# shift = int(input("Type the shift number: \n"))

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encrypted text is {cipher_text}")


def decrypt(encrypt_text, shift_amount):
    plain_text = ""
    for letter in encrypt_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    message = input("enter message to be encrypted: \n").lower()
    shift = int(input("Type the shift number: \n"))
    encrypt(plain_text=message, shift_amount=shift)
elif direction =="decode":
    message = input("enter message to be decrypted: \n").lower()
    shift = int(input("Type the shift number: \n"))
    decrypt(encrypt_text= message, shift_amount=shift)
else:
    print("invalid input")
