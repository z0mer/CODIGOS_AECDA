# Análise do Pseudocódigo (21.08.2024)

```
INSERTION-SORT(V, n)                #c1
  para i = 1 ate n                  #c2 = n
    chave = V[1]                    #c3 = n  
    //insira na posicao correta     #c4 = --  
    j = i - 1                       #c5 = n
    enquanto j >= 0 e V[j] > chave  #c6 = n
      V[j + 1] = V[j]               #c7 = 0
      j = j - 1                     #c8 = 0
    V[j + 1] = chave                #c9 = 0
```
