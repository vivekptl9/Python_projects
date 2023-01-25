import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:
        yn = input("Did you mean %s instead ? \nPlease Enter Yes or No to confirm:  " % get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "no":
            return "The word does not exist, please check again."
        else:
            return "We did not understand your query."
    else:
        return "The word does not exist, please check again."
word = input("Enter word: ")
output = translate(word)
count=1
if type(output) == list:
    for item in output:
        iter = count
        count+=1
        print(f"{iter}. {item}")
else:
    print(output)   
