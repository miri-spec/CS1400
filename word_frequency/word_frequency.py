def word_count(file):
    frequencies = {}
    f = open(file , 'r')
    text = f.read()
    words = text.split()
    for word in words:
        if frequencies.get(word , False) == False:
            frequency = words.count(word)
            frequencies[word] = frequency
    word_keys = list(frequencies.keys())
    word_keys.sort()
    for key in word_keys:
        print(key, frequencies[key])

if __name__ =="__main__":
    filename = input("Enter the input file name: ")
    word_count(filename)