alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(text, shift, direction):
    split_text = list(text)
    index_alphabet = []
    for txt in split_text:
        if txt in alphabet:
            index_text = alphabet.index(txt)
            index_alphabet.append(index_text)
        else:
            index_alphabet.append(txt)
    caesar_list_index = []
    for x in index_alphabet:
        if type(x) == int:
            if direction == "encode":
                x += shift
            elif direction == "decode":
                x -= shift
            caesar_list_index.append(x)
        else:
            caesar_list_index.append(x)

    text_caesar = ""
    for i in caesar_list_index:
        if type(i) == int:
            text_caesar += alphabet[i]
        else:
            text_caesar += i
    print(f"The {direction} text is {text_caesar}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % 26
    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again.otherwise type 'no'..\n")
    if result == "no":
        should_continue = False
        print("good by sir...")
    else:
        should_continue = True
