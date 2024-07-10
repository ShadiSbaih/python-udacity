def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False
    


def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append([index,index + len(sub)])
            index += len(sub)
        else:
            index += 1
    return matches
    
    
lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

def breakify(strings):
    return "<br>".join(strings)
  
print(breakify(lines))
    
print(locate_all('yesyesyes', 'yes'))

string = "Hello world!"
output = []
index = 0
while index < len(string):
    output.append(string[index])
    index += 1

print(output)

# if(is_substring("ad","shadi")==True):
#     print("yes")


def remove_substring(string, substring):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)