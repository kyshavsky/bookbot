def count_words(text):
    num_words = 0
    for word in text.split():
        num_words +=1
    return num_words

def count_char(text):
    char_dict = {}
    

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
    
   
# if __name__ == "__main__":
#     result = count_char("hello") 
#     print(result)
   

