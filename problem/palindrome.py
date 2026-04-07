def is_palindrome(text):
    #Check if a string is a palindrome.
    return text == text[::-1]


if __name__ == "__main__":
    word = input("Enter a word: ")
    print("Palindrome" if is_palindrome(word) else "Not palindrome")
