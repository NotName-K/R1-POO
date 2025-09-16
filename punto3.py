def prim(a: list[str]) -> list[int]:
    z = []
    for i in a: 
        n = int(i)  
        for y in range(2, int(n**0.5) + 1):
            if n % y == 0:
                z.append(i) 
    
    for i in z:
        if i in a:
            a.remove(i)

    return(a)

if __name__ == "__main__":
    a = input("Lista de Numeros enteros: ")
    b = a.split(",")  
    print(prim(b))
