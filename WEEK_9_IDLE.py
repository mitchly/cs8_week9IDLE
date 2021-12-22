#using modulo to cycle through a list
def getAdvice(num):

    stepsToSuccess = [ "Keep track of deadlines", \
                     "Read the book", \
                     "Do the homework yourself", \
                     "Attend lectures", "Ask questions", \
                     "Attend labs", "Enjoy studying" ]
    
    if num > 0 :
        advice = stepsToSuccess[num % len(stepsToSuccess)]
        return advice
    elif num < 0 :
        return None
    else:
        advice = stepsToSuccess[num]
        return advice
#encryption
def simpleEncode(plaintext, alphabet, cipher):
    ciphertext = ''
    if len(alphabet) != len(cipher):
        return -1
    else:
        for character in plaintext:
            index = alphabet.find(character)
            if index == -1:
                return None
            else:
                ciphertext += cipher[index]
        return ciphertext	
#decryption
def simpleDecode(ciphertext, alphabet, cipher):
    plaintext = ''
    if len(alphabet) != len(cipher):
        return -1
    else:
        for character in ciphertext:
            index = cipher.find(character)
            if index == -1:
                return None
            else:
                plaintext += alphabet[index]
        return plaintext	
#url_structure
def url_structure(url_tuple):
    url = ''
    for contents in url_tuple:
        if url_tuple.index(contents) == 0:
            url += str(contents) + "://"
        else:
            url += str(contents)
    print("The URL scheme for {} is {}, and it is the 0th position of the tuple.".format(url,url_tuple[0]))
    print("The URL netloc for {} is {}, and it is the 1st position of the tuple.".format(url,url_tuple[1]))
    print("The URL path for {} is {}, and it is the 2nd position of the tuple.".format(url,url_tuple[2]))
    print("The URL param for {} is {}, and it is the 3rd position of the tuple.".format(url,url_tuple[3]))
    print("The URL query for {} is {}, and it is the 4th position of the tuple.".format(url,url_tuple[4]))
    #TA said to print param and not fragment
    return url

if __name__ == "__main__": 
    from urllib.parse import urlparse
    o = urlparse('https://www.ucsb.edu/') #parse a URL into components that can be indexed by tuple position or as an attribute
    print(o)
    print(o.geturl())
    print(o.scheme) #scheme
    print(o[0]) #scheme
    print(o.netloc) #network location
    print(o[1]) #network location
    print(o.path) #path
    print(o[2]) #also print a path
    url_structure(o) #print out the url structure


