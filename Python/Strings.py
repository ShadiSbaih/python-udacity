def count_character(string, target):
    count = 0
    for ch in string:
        if ch == target:
            count = count + 1
    return count
   
print(count_character("saleem","e"))
