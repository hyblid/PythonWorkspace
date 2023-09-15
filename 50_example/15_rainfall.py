import collections as collection

def rainfall():
    rainfall = collection.defaultdict(int)
    while True:
        city = input("Enter city: ")
        if not city:
            break
        
        mm_rain = int(input("Rain:"))
        rainfall[city] +=  mm_rain

    for city, rain in rainfall.items():
        print(f"{city}:{rain}")
        
def rainfall2():
    rainfall={}
    while True:
        city = input("Enter city: ")
        if not city:
            break
        
        mm_rain = int(input("Rain:"))
        if city not in rainfall:
            rainfall[city] = []
        rainfall[city].append(mm_rain)

    for city, rain in rainfall.items():
        print(f"city{city}:total{sum(rain)}:average{sum(rain)/len(rain)}")
        
def errorLog():
    error_log ={}
    for line in open("apach_err_log.txt"):
        line_log = line.split()
        error_code = str(line_log[5])
        if error_code not in error_log:
           error_log[error_code]=[]
        error_log[error_code].append(line_log[0])
    print(error_log)
    
def word_length():
    words_length = {}
    for word in open("30words.txt"):
        word = word.replace("\n", "")
        index = str(len(word))
        if index not in words_length:
           words_length[index]=[]
        words_length[index].append(word)
    
    for k in words_length:
        print(f"word length {k} and occurance {len(words_length[k])}")    
    
def word_lengths():
    output = collection.defaultdict(int)

    for one_line in open("30words.txt"):
        for one_word in one_line.split():
            one_word = one_word.replace("\n", "")
            output[len(one_word)] += 1
    
    print(output)  

    """
    1. assing  output = collection.defaultdict(int)  
       if you want to add something same key
       
       output[key] += 1

       if you want to add into list of same key
       
           if index not in words_length:
              words_length[index]=[] ----> assign key's list
           words_length[index].append(word)
     
    """