
def consonant_value(string):
    vowels = "aeiou"
    result = []
    list = []
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
    for string in result:
        value = 0
        for letter in string:
            value += (ord(letter) - 96)
        list.append(value)
    list.sort(reverse=True)
    return list[0]

    
print(consonant_value("strength"))



