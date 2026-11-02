from morse_translation import MORSE_DICT

def produce_morse_code(user_input):
#(There is no distinction between upper and lower case - all characters are treated as capitals.)
    text = user_input.upper()

    translated_text = ''
    #Validation: Make sure the character exists in the morse code dictionary first.
    for character in text:
        if character in MORSE_DICT:
            translated_text += MORSE_DICT[character] + ' '

    return translated_text


#This is for IF the user wants to convert it back to NORMAL text: (This is going to be a seperate function on its own)
    # alpha_letters_list = list(translated_text.split(' '))
    # back_to_string = ''
    # for item in alpha_letters_list: #Each morse code representing a letter
    #     key_for_value = [letter for letter, morse in morse_code.items() if item == morse]
    #     if key_for_value:
    #         back_to_string += key_for_value[0]










#before:
# user_input = user_input
#     translated_text = ''
#     #Validation: Make sure the character exists in the morse code first.
#     for character in user_input:
#         if character in morse_code:
#             translated_text += morse_code[character] + ' '

#     alpha_letters_list = list(translated_text.split(' '))

#     translate = input(f"Would you like to convert this morse code {translated_text}, into text? (Y/N): ").upper()

#     # If they type anything else, end the program (or you might just bring them back to the home page)
#     if translate == 'Y':
#         back_to_string = ''
#         for item in alpha_letters_list: #Each morse code representing a letter
#             key_for_value = [letter for letter, morse in morse_code.items() if item == morse]
#             if key_for_value:
#                 back_to_string += key_for_value[0]
#         print(f"Morse code converted back to text: {back_to_string}")   