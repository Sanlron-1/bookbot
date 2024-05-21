
def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
              
    wordcount = countWords(file_contents)
    output = countLetters(file_contents)
    output.sort(reverse=True, key=sort_on)

    print(f'--- Begin report of {file} ---')
    print(f'{wordcount} words found in the document\n')
    for item in output:
        #print(f'{item.name}')
        print(f'The %s character was found %d times.' % (item["name"], item["num"]))
        #...

def countWords(input):
    words = input.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def countLetters(input):
    lowered_letters = input.lower()
    alphabet = set()
    temp_list = []
    dictionary = {}
    for l in lowered_letters:
        if l.isalpha():
            alphabet.add(l)
        else:
            #print(f'{l} failed')
            pass
    
    for a in alphabet:
        dictionary[a] = lowered_letters.count(a)
        #dictionary['name'] = dictionary[a]
        #dictionary['num'] = lowered_letters.count(a)

    temp_list = convert_dict(dictionary)
    return temp_list 
    #print(alphabet)
    
def convert_dict(dict):
    output_list = [{'name': key, 'num':value} for key, value in dict.items()]
    return output_list


main()