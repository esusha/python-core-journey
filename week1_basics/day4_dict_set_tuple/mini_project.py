# Write a function most_frequent_word(text: str) -> tuple
# Return the word that occurs most and its count.

def most_frequent_word(text: str) -> tuple:
    """
    Returns the most frequent word and its count from the given text.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    tuple: A tuple containing the most frequent word and its count.
    """
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Count the occurrences of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Find the most frequent word and its count
    most_frequent = max(word_count.items(), key=lambda item: item[1])
    
    return most_frequent

# Example usage
text = "apple banana apple orange banana apple"
result = most_frequent_word(text)
print(result)
print(f"The most frequent word is '{result[0]}' with a count of {result[1]}.")