def main():
    text = read_file()
    report(count_words(text), count_chars(text))

def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1
    return char_dict

def report(word_count, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    char_list = []
    for key in char_dict:
        new_dict = {"char": key, "num": char_dict[key]}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    for dict in char_list:
        char = dict["char"]
        num = dict["num"]
        print(f"The {char} character was found {num} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()