def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]


mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']
shortsstringlist = shorten(mystringlist)
result = []
try:
    s = next(shortsstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(list(filter(lambda letter: letter in 'aeiou', s)))
        # Truncate the next string depending
        # on the number of vowels in the previous one
        s = shortsstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass

print(result)