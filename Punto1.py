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