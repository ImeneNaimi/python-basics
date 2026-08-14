text="Artificial Intelligence"
print(text[0])
print(text[-1])
print(len(text))

name=input("What's your name")
print(name.upper())
print(name.lower())

sentence=input("Enter a sentence")
for letter in sentence:
    print(letter)

Sentence="I love Python"
print(Sentence.replace("Python","AI"))

phrase=input("Enter a sentence")
words=phrase.split()
print(words)

sen=input("Enter a sentence: ")
print(sen.count("a"))

mail=input("Enter your email adress:")
if mail.endswith(".com"):
    print("Valid input")
else:
    print("Invalid domain!")

sent=input("Enter a sentence")
for i in range(len(sent)-1,-1,-1):
    print(sent[i],end="")

