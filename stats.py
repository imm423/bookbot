def word_counter(book_text):
    all_words = book_text.split()
    word_count = len(all_words)
    return word_count

def char_counter(book_text):
    lowercase_text = book_text.lower()
    char_count = {}
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def getnum(get_num_from):
    return get_num_from["num"]



def char_sort(unsorted_dict):
    titled_dict = {}
    dict_list = []

    for i in unsorted_dict:
        titled_dict[i] = {"char": i, "num": unsorted_dict[i]}
        dict_list.append(titled_dict[i])
    
    dict_list.sort(reverse=True, key=getnum)
    
    return dict_list




