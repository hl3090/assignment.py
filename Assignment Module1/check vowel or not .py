check_alphabet = input("Enter an Alphabet: ")

vowels = 'a','e','i','o','u'

if check_alphabet in vowels:
    print ("It is a vowel")
elif check_alphabet.isalpha():
    print ("It is a consonant")
else:
    print ("Error")