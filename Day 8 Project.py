import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'] * 2


def caesar(ciphertext, shift_amount, cipher_direction):
    new_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for lett in ciphertext:
        if lett in alphabet:
            new_text += alphabet[alphabet.index(lett) + shift_amount]
        else:
            new_text += lett
    print(f"The {cipher_direction}d text is: {new_text}")


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Please type 'encode', or 'decode'!")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        print("Sorry! The shift must be 26 or under!")
        continue
    caesar(text, shift, direction)
    game_on = True
    while True:
        userinput = input("Type 'yes' if you want to go again, 'no' if you want to exit.")
        if userinput.lower() == 'yes':
            break
        elif userinput.lower() == "no":
            print("Goodbye!")
            game_on = False
            break
        else:
            print("Not a valid input!")
            continue
    if not game_on:
        break
