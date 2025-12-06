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



def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_char_dict):
   final_list = []
   for k,v in num_char_dict.items():
        small_dict = {"char": k, "num": v}
        final_list.append(small_dict)

   final_list.sort(reverse=True, key=sort_on)
   return final_list
   


    
   








    
   
# if __name__ == "__main__":
#     dict = count_char("hello I am a person I love pizza") 
#     result = chars_dict_to_sorted_list(dict)
#     print(result)
   

