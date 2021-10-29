def user_input():
    user_string = input("Enter any string")
    return user_string

def modify_text():
    original_string = user_input()
    temp_string = original_string.split()
    for index, letter in enumerate(original_string, 1):
        print(index, ':', letter)
        print(temp_string)
        last_char = original_string[-1]
        print(last_char)
        without_last_char = original_string[:-1]
        print(without_last_char)

if __name__ == "__main__":




    def modify_text2():
        original_string_2 = user_input()
        original_string_2
        modify_text()

        multiline = '''Line #1
        Line #2'''

        print(len(multiline))


    # Function to convert a word to its PigLatin form
    def pigLatin(s):
        flag = False;
        vow_index = 0
        for i in range(len(s)):
                vow_index = i
                flag = True;
                break;
        if (not flag):
            return s;
        pigLatin = s[vow_index:] + s[0:vow_index] + "ay"
        return pigLatin


    # Initializing a sentence
    sentence = "I like to play basketball."
    # Splitting the sentence into a list consisting of its words
    list = sentence.split()
    # Printing the original sentence
    print("The original sentence is:-")
    print(sentence)
    # Initialising an empty string for forming the PigLatin sentence
    pig_str = ""
    # Iterating over list
    for word in list:
        pig_str += " " + pigLatin(word)
    # Printing the PigLatin sentence
    print("The piglatin sentence is:-")
    print(pig_str)