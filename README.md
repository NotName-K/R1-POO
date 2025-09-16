# R1-POO
## 5 puntos de pdc basicos.
### 1. Operaciones basicas con entrada (1,2,"+")
Este programa recibe una lista de tres elementos: dos números y un operador (+, -, *, /). Convierte los números a  un float y aplica la operación indicada.

Devuelve un número o un mensaje de error si hay una división por cero, un operador es invalido o entrada mal escrita.

```python
def  sumaa(a: list[str]) -> float | str:   
   if len(a) == 3: 
      if a[2] == '+':
        x = float(a[0]) + float(a[1])
      elif a[2] == '-':
        x = float(a[0]) - float(a[1])
      elif a[2] == "*":
        x = float(a[0]) * float(a[1])
      elif a[2] == "/":
        if float(a[1]) != 0:
         x = float(a[0]) / float(a[1])
        else:
         x = "Error: División por cero"       
      else:
        x = str("Error")
      return x
 
if __name__ == "__main__":
    a = input("Ingresa valores (de forma 1,2,+):  ")
    b = a.split(",")
    print(sumaa(b))
```

### 2. Palindromos
Compara dos frases ingresadas, empieza descartando a partir de la cantidad de letras.
Si son iguales, luego compara el orden de las letras, entrega si son o no segun si cumple   ambos requisitos.


```python
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

```

### 3.Numeros Primos
Se recibe una lista de enteros, luego se filtra cada numero par y se agrega a la lista z, por ultimo se remueven los valores en comun entre listas en la lista original, quedando la lista de primos. 
```python
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
```

### 4. Mayor suma de consecutivos 

recibe una lista de números, calcula la suma de cada par de elementos consecutivos, se guarda esos resultados en una lista aparte, y ordenado de menor a mayor, devuelve el valor más alto de dichas sumas. Si la lista contiene un solo número, retorna "Error" porque no hay pares para sumar.

```python
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
```
### 5. Palabras con mismos caracteres

Recibe una lista de palabras, se les quita espacios extra y las pasa a minúsculas.
Luego convierte cada palabra en una lista de letras ordenadas y compara todas las posibles parejas. 
Si dos palabras tienen las mismas letras, se guardan juntas en la lista de resultados, que finalmente se entrega al usuario.

```python
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
```
