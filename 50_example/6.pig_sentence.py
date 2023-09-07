def pl_sentence1(w):
    output=""
    word_list=w.split(" ")
    for word in word_list:
        if word[0] in "a,e,i,o,u":
            output+= f"{word}way "
        output+= f'{word[1:]}{word[0]}ay ' 
    print(output)

def pl_sentence2(filename="example.txt"):  
    output = []

    for n, one_line in enumerate(open(filename)):
        words = one_line.split()

        if not words:
            continue

        if n >= 10:
            break

        if n >= len(words):
            output.append(words[-1])
        else:
            output.append(words[n])

    return "".join(output)

    """
    ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    """
def pl_sentence3():
    #["abc def ghi","jkl mno pqr","stu vwx yz"]
    list_of_words = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    return [' '.join(t)
            for t in (zip(*[s.split() for s in list_of_words]))]
    
    print(output)
    
def ips_for_404s(filename):
    for one_line in open(filename):
        if ' 404 ' in one_line:
            print(one_line.split()[0])   
                                                                      
    
print(pl_sentence3())