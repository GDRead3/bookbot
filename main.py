def main():
    print ("Hello, I'm a book bot! I can read a text file and tell you how many words and characters are in it.")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_text = turn_lowercase(text)
    characters_dict = count_characters(lowered_text)
    print ("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    # Sort dictionary items by count in descending order
    sorted_chars = sorted(characters_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print ("--- End report ---")


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
        if char.isalpha():
            if char in characters:
                characters[char] = characters[char] + 1
            else:
                characters[char] = 1
    return characters


main()
