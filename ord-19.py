# 19. Python Program to Sort Words in Alphabetic Order

sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("Sorted words:", " ".join(words))