def prim(a):
    if len(a) > 1:
        z = []
        for i in range(len(a)-1):
            p = int(a[i]) + int(a[i+1])   
            z.append(p)
        p = sorted(z)[-1]  
    else: 
        p = "Error"
    return p
    
if __name__ == "__main__":
    a = input("Lista de Numeros enteros: ")
    b = a.split(",")  
    print(prim(b))