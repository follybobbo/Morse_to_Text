logo = r"""
   _____                                 ________                                   __                
  /     \   ___________  ______ ____    /  _____/  ____   ____   ________________ _/  |_  ___________ 
 /  \ /  \ /  _ \_  __ \/  ___// __ \  /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
/    Y    (  <_> )  | \/\___ \\  ___/  \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
\____|__  /\____/|__|  /____  >\___  >  \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/                  \/     \/          \/     \/     \/     \/           \/                   
"""

"""create dictionary below it should contain letter as key, and morse code interpretation as value"""
text_morse_dictionary = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "0": "_____",
    "1": ".____",
     2: "..___",
     3: "...__",
     4: "...._",
     5: ".....",
     6: "_....",
     7: "__...",
     8: "___..",
     9: "____.",
}

morse_list = []
text_list = []

"""Write code below that will take input and convert it to morse code"""
def text_to_morse():
    word = input("Please input word you want to convert to Morse. \n")
    word_upper = word.upper()

    """Split the sentence entered by user into words"""
    word_list = word_upper.split()

    """loop through the dictionary which contains the alphabet and it respective morse code translation, and
    get the value for the key. the value pair is then stored in a list, with the space appended signalling the 
    start of a new word. list containing the morse code is returned by thus function."""
    for word in word_list:
        for letter in word:
            morse_letter = text_morse_dictionary.get(letter)
            morse_list.append(f"{morse_letter} ")
        morse_list.append("  ")

    return morse_list


"""Converts morse code input by user to human readable text"""
def morse_to_text():
    morse = input("Please input morse code you want to decode. \n")
    #because it was designed for each word in the morse code is separated by 3 spaces
    #Hence we split the user input, using three spaces as the key to our splitting.
    split_morse = morse.split("   ")

    #loop through the list of sentence and split each word into letters, note each letter in a word is separated by a space.
    for word in split_morse:
        split_word = word.split(" ")
        #for each letter in the word, the text_morse_dictionary is looped through, if the morse letter matches with any
        # value, its key is stored in a list text_list
        for morse_letter in split_word:
            for key, value in text_morse_dictionary.items():
                if value == morse_letter:
                    text_list.append(key)

        #space is added every word has been translated, for easy transformation into sentences.
        text_list.append(" ")


    return text_list



def main():
    print(logo)

    decode_or_code = input("Do you want to Decode or Encode ? ('Decode/Encode'): ")
    #turns every word the user inputs into capital letter for easy search through the text_morse_dictionary
    capitalised = decode_or_code.capitalize()

    if capitalised == "Encode":
        list_morse = text_to_morse()
        morse_translation = "".join(list_morse)
        print(morse_translation)
    elif capitalised == "Decode":
        list_text = morse_to_text()
        text_translation = "".join(list_text)
        print(list_text)
    else:
        print("Wrong option chosen.")
        print("\n" * 10)
        main()

main()


