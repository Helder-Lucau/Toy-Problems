
def consonant_value(string):
    vowels = "aeiou"
    result = []
    temp = ""
    for char in string.lower():
        if char in vowels:
            if temp != "":
                result.append(temp)
                temp = ""
        else:
                temp += char
    if temp != "":
                result.append(temp)
    # return result
    for string in result:
        for ch in string:
              print(ord(ch) - 96)
    
print(consonant_value("strength"))



