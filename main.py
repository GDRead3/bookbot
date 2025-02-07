def main():
    print("Hello, I'm a book bot! I can read a text file and tell you how many words and characters are in it.")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_text = turn_lowercase(text)
    
    print("\nWhat would you like to do?")
    print("1. View character count analysis")
    print("2. Search for a specific word")
    print("3. Both")
    choice = input("Enter your choice (1-3): ")
    
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    if choice in ['1', '3']:
        characters_dict = count_characters(lowered_text)
        print("Would you like to sort the characters in order of frequency or in alphabetical order? (f = frequency, a = alphabetical)")
        sort_choice = input()
        
        if sort_choice.lower() == "f":
            # Sort dictionary items by count in descending order
            sorted_chars = sorted(characters_dict.items(), key=lambda x: x[1], reverse=True)
            for char, count in sorted_chars:
                print(f"The '{char}' character was found {count} times")
        elif sort_choice.lower() == "a":
            # Sort dictionary items in alphabetical order
            sorted_chars = sorted(characters_dict.items(), key=lambda x: x[0].lower())
            for char, count in sorted_chars:
                print(f"The '{char}' character was found {count} times")
        else:
            print("Invalid option selected... skipping character analysis")
        print()
        
    if choice in ['2', '3']:
        search_word = input("Enter a word to search for: ").lower()
        word_count = count_word(lowered_text, search_word)
        print(f"The word '{search_word}' appears {word_count} times\n")
    
    print("--- End report ---")


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

def count_word(text, word):
    words = text.split()
    return words.count(word)

main()
