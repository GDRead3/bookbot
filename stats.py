def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    # Convert text to lowercase to count all variations of each letter
    text = text.lower()
    
    # Create a dictionary to store letter counts
    letter_counts = {}
    
    # Count each letter
    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    return letter_counts 