def get_book_text(file_path):
    with open(file_path) as f:
        data = f.read()

    return data

def word_count(file_path):
    contents = get_book_text(file_path)
    words = contents.split()
    count = 0

    for word in words:
        count += 1
    
    return count

def char_count(file_path):
    contents = get_book_text(file_path)
    num_ch = {}

    for char in contents:
        char = char.lower()
        if char in num_ch:
            num_ch[char] += 1
        else:
            num_ch[char] = 1
    
    return num_ch

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []
    
    for ch in dict:
        ch_dict = {"char":ch,"num":dict[ch]}
        dict_list.append(ch_dict)

    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list