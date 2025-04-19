# Write a function word_summary(text: str) that returns:

# Total number of words

# Total characters (excluding spaces)

# Count of each word (using dict)

def word_summary(text: str) -> dict:
    """
    Returns a summary of the text including total words, total characters (excluding spaces), and word count.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary containing the total number of words, total characters (excluding spaces), and word count.
    """
    
    # Split the text into words
    words = text.split()
    
    # Count the total number of words
    total_words = len(words)
    
    # Count the total number of characters excluding spaces
    total_characters = len(text.replace(" ", ""))
    
    # Count each word using a dictionary
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return {
        "total_words": total_words,
        "total_characters": total_characters,
        "word_count": word_count
    }

print(word_summary("This is a test. This test is only a test."))