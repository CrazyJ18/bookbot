def main():
    text = read_file()
    print(f"{count_words(text)} words in document")

def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

main()