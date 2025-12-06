# def get_book_text(book_path):
#     with open(book_path) as f:
#         file_contents = f.read()
#     print(file_contents)
    

def count_words(book_path):
    num_words = 0
    with open(book_path) as f:
        file_contents = f.read()
        word_split = file_contents.split()
        #print(word_split)
    for word in word_split:
        num_words +=1
    print(f"Found {num_words} total words")


    




count_words("/home/kylev/workspace/github.com/kylev/bookbot/books/frankenstein.txt")

