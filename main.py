def main():
    print("Hello, I'm a book bot! I can read a text file and tell you how many words and characters are in it.")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_text = turn_lowercase(text)
    
    print("\nWhat would you like to do?")
    print("1. View character count analysis")
    print("2. Search for a specific word")
    print("3. View most common words")
    print("4. All of the above")
    choice = input("Enter your choice (1-4): ")
    
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    if choice in ['1', '4']:
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
        
    if choice in ['2', '4']:
        search_word = input("Enter a word to search for: ").lower()
        word_count = count_word(lowered_text, search_word)
        print(f"The word '{search_word}' appears {word_count} times\n")
    
    if choice in ['3', '4']:
        print("Most common words analysis:")
        word_counts = count_most_common_words(lowered_text)
        num_words_to_show = int(input("How many top words would you like to see? "))
        print(f"\nTop {num_words_to_show} most common words:")
        for word, count in word_counts[:num_words_to_show]:
            print(f"'{word}' appears {count} times")
        print()
    
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

def count_most_common_words(text):
    # List of common English words to exclude
    stop_words = {'the', 'and', 'to', 'of', 'i', 'a', 'in', 'was', 'that', 'had', 'is', 'it', 'for', 'you', 'he', 'be', 'with', 'on', 'at', 'by', 'not', 'this', 'but', 'they', 'his', 'from', 'she', 'her', 'were', 'my', 'as', 'what', 'their', 'has', 'would', 'there', 'been', 'have', 'which', 'when', 'who', 'will', 'more', 'if', 'no', 'out', 'so', 'up', 'all'}
    
    # Split text into words and remove punctuation
    words = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('"', '').replace(';', '').replace(':', '').split()
    
    # Count words excluding stop words
    word_counts = {}
    for word in words:
        if word.isalpha() and word not in stop_words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    # Sort by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

main()
