import sys

def decipher_words(args):
    words = [word[0] for word in args.split() if word.isalpha()]
    return ''.join(words)

input_string = ' '.join(sys.argv[1:])
result_string = decipher_words(input_string)
print(result_string)
