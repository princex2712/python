# Write a Python program to count the occurrences of each word in a
# given sentence
sentence = " Hello, How are you doing, Hello?"
words = sentence.split()
occurrences = {}

for word in words:
    optimised_word = word.strip('.,?!').lower()

    if optimised_word in occurrences:
        occurrences[optimised_word] +=1
    else:
        occurrences[optimised_word] = 1

for word,count in occurrences.items():
    print(f"{word}:{count} ")