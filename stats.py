def get_num_words(text):
    return len(text.split())

def count_characters(text):
    dict = {}
    lower_text = text.lower()

    for char in lower_text:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict.update({char: 1})

    return dict

def get_sorted_list(dict):
    sorted_list = []
    for d in dict:
        new_dict = {}
        if d.isalpha():
            new_dict["char"] = d
            new_dict["num"] = dict[d]
            sorted_list.append(new_dict)

    sorted_list.sort(key=lambda x: x['num'],reverse=True)

    return sorted_list
