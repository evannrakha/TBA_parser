S = ['kamu', 'kau', 'anda', 'saya', 'aku']
P = ['makan', 'minum', 'mengajar', 'mengejar', 'baca']
O = ['roti', 'kopi', 'fisika', 'buku', 'susu']
K = ['di kantin', 'di kafe', 'di kelas','di taman', 'di rumah']


def isSubject(word):
    for kata in S:
        if word == kata:
            return True
            break
    return False

def isPredikat(word):
    for kata in P:
        if word == kata:
            return True
            break
    return False
        
def isObjek(word):
    for kata in O:
        if word == kata:
            return True
            break
    return False

def isKeterangan(word):
    for kata in K:
        if word == kata:
            return True
            break
    return False


def recognizer(sentence):
    stack = []
    words = []
    struk = []
    words = sentence.split()
   
    if len(words) >= 4:
        words[-2] = words[-2] + " " + words[-1]
        words = words[:-1]

    words.append('n')
    print(words)
    print("Isi Stack:")

    stack.append('#')
    print(stack)

    stack.append('@')
    i = 0
    while stack[-1] != '#':
        print(stack)
        match stack[-1]:
            case '@':
                if isSubject(words[i]):
                    stack.pop()
                    stack.append('X')
                    stack.append('p')
                    stack.append('s')
                else:
                    print("struktur ERROR")
                    break
            case 'X':
                if isObjek(words[i]):
                    stack.pop()
                    stack.append('Y')
                    stack.append('o')
                elif isKeterangan(words[i]):
                    stack.pop()
                    stack.append('Y')
                    stack.append('k')
                elif words[i] == 'n':
                    stack.pop()
                else:
                    print("Struktur ERROR")
                    break
            case 'Y':
                if isKeterangan(words[i]):
                    stack.pop()
                    stack.append('k')
                elif words[i] == 'n':
                    stack.pop()
                else:
                    print("Struktur ERROR")
                    break
            case 's':
                if isSubject(words[i]):
                    struk.append(stack.pop())
                    i += 1
                else:
                    print("Struktur ERROR")
                    break
            case 'p':
                if isPredikat(words[i]):
                    struk.append(stack.pop())
                    i += 1
                else:
                    print("Struktur ERROR")
                    break
            case 'o':
                if isObjek(words[i]):
                    struk.append(stack.pop())
                    i += 1
                else:
                    print("Struktur ERROR")
                    break
            case 'k':
                if isKeterangan(words[i]):
                    struk.append(stack.pop())
                    i += 1
                else:
                    print("Struktur ERROR")
                    break
    stack.pop()
    if len(stack) == 0:
        print(stack)
        print("Struktur diterima")
        print("Struktur: ", end='')
        for i in struk[:-1]:
            print(f"{i} - ", end='')
        print(struk[-1], "\n")
    else:
        print("Terdapat struktur kata yang error")
        print(stack)


print("Kamus yang tersedia") 
print(f"Subject : {S}")
print(f"Predikat: {P}")
print(f"Object: {O}")
print(f"Keterangan: {K}")      
print("Strutur yang di terima:")
print("s - p - o - k")
print("s - p - k")
print("s - p - o")
print("s - p")      
kalimat = input("Kalimat: ")
recognizer(kalimat)


        

            


    
    
