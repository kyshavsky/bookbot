from stats import count_words, count_char, chars_dict_to_sorted_list
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
    
    chars = count_char(text)
    sorted_chars = chars_dict_to_sorted_list(chars)

    for item in sorted_chars:
        char = item["char"]
        if not char.isalpha():
            continue
        num = item["num"]
        print(f"{char}: {num}")


    


if __name__ == "__main__":
    main()


    






