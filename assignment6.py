


def string_parcer(sentence):
    # split the sentence into multiple words
    list_of_words = sentence.split(" ")

    # return the list
    return list_of_words
    # declare the list
list_of_words = []

def main():
 


    # greet the user
 print(
        "This program will ask the user for a sentence and then display each word, without spaces, one per line."
    )

    # get the user input
 sentence = input("Enter a sentence: ")

    # call the function
 list_of_words = string_parcer(sentence)
 
 
 def print_in_a_frame(words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))

 print_in_a_frame(list_of_words)
 sentence.split("\n") 
 
    # display the output to the user
if __name__ == "__main__":
   main()
