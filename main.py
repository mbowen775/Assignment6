import sys


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


    def string2() -> str:
        str1 = str("");
        if len(sys.argv) > 1:
            str1 = sys.argv[1];
        else:
            str1 = input("enter user sentence for string2: ");
        str1 = list(str1.split(" "));
        for i in range(len(str1)):
            word = str1[i];
            if word[0] not in ['a', 'e', 'i', 'o', 'u']:
                temp = word[1:] + word[0];
                word = temp;
                word += "ay"
            else:
                word += "yay"
            str1[i] = word;
        return " ".join(str1);


    def breakIntoWords(string) -> list:
        return list(string.split(" "));


    def printwords(lst):
        for i in lst:
            print(i);


    def string3():
        str1 = str("");
        if len(sys.argv) > 1:
            str1 = sys.argv[1];
        else:
            str1 = input("enter user sentence for string3: ");

        printwords(breakIntoWords(str1));


    print(string2())
    string3()
    # Printing the original sentence
    print("The original sentence is:-")
    print(sentence)
    # Initializing an empty string for forming the PigLatin sentence
    pig_str = ""
    # Perform over list
    for word in list:
        pig_str += " " + pigLatin(word)
    # Printing the piglatin sentence
    print("The piglatin sentence is:-")
    print(pig_str)

    import re

    x = re.search("dog", "A dog and a cat can't be friends.")
    print(x)

    x = re.search("bird", "A dog and a cat can't be friends.")
    print(x)

    if re.search("cat", "A dog and a cat can't be friends."):
        print("Some kind of dog has been found :-)")
    else:
        print("No dog has been found :-)")

    if re.search("bird", "A dog and a cat can't be friends."):
        print("Dogs and Cats and a bird.")
    else:
        print("No bird around.")

import os
import platform

print(os.name)
print(platform.system())
print(platform.release())

