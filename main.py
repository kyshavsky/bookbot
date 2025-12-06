from stats import count_words
#Function pulls book text from txt file

def get_book_text(book_path): #funciton name
    with open(book_path) as f: #finds book path and opens file
        file_contents = f.read() #reads content file and saves to a new variable
    return file_contents #prints contents of file

def main():
    book_path = "/home/kylev/workspace/github.com/kylev/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()


    






