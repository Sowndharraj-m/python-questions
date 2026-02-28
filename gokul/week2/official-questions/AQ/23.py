# Problem-23: Accept a paragraph as input and find the number of sentences in it.
# Assume that full stops are the only sentence breaks.

paragraph = input("Enter a paragraph: ")

# Count the number of full stops (sentences)
sentence_count = paragraph.count('a')

print("Number of sentences:", sentence_count)
