def save_summary(text, filename):
	words = text.split()
	word_count = len(words)
	characters = text.replace(" ", "")
	characters_count = len(characters)
	with open(filename, "w") as f:
		f.write(f"word_count = {word_count}\n")
		f.write(f"characters_count = {characters_count}\n")
		
if __name__ == "__main__":
    text = "Hello World"
    filename = "summary.txt"
    save_summary(text, filename)
    print("Summary saved to summary.txt")