def palin(a: str, b: str) -> str:
    if len(a) != len(b):
        return "No son palindromos"
    
    for i in range(len(a)):
        if a[i] != b[-i-1]:
            return "No son palindromos"
    
    return "Son palindromos"

if __name__ == "__main__":
    a = input("Ingresa la palabra 1: ").lower()
    b = input("Ingresa la palabra 2: ").lower()
    print(palin(a,b))