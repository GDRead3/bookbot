def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    lowered_text = turn_lowercase(text)
    characters_dict = count_characters(lowered_text)
    print (characters_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def turn_lowercase(text):
    return text.lower()

def count_characters(text):
    characters = {}
    for char in text:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1
    return characters


main()
