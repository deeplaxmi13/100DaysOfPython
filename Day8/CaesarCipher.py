from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


# def encrypt(plain_text,shift_amount):
#     cipherText = ""
#     for char in plain_text:
#         position = alphabet.index(char)
#         newPos = position + shift_amount
#         newLetter = alphabet[newPos]
#         cipherText += newLetter
#     print(f"The encoded text is {cipherText}")



# def decyrpt(cipher_text,shift_amount):
#     decryptedText = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         newPos = position - shift_amount
#         newLetter = alphabet[newPos]
#         decryptedText += newLetter
#     print(f"Your decoded text is {decryptedText}")

# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction == "decode":
#     decyrpt(cipher_text=text, shift_amount=shift)
# else:
#     print("You entered a wrong choice")
        

def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            newPos = position + shift_amount
            end_text += alphabet[newPos]
        else:
            end_text += char
    print(f"Your {cipher_direction} text is {end_text}")

should_continue= True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message: \n").lower()

    shift = int(input("Enter the shift number: \n"))

    shift = shift % 26

    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)

    result = input("Type 'yes' if you want to g again. Otherwise type 'no' :\n").lower()
    if result == "no":
        should_continue = False
        print("Good Bye!!")
    
            
        



