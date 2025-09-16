def same(a: list[str]) -> list[list[str]]:
    k = [i.strip().lower() for i in a]              
    l = [sorted(list(i)) for i in k]        
    o = []                                  

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                o.append([a[i], a[j]])      

    return o

if __name__ == "__main__":
    a = input("Escribe tu lista: ")
    b = a.split(",")
    print(same(b))
