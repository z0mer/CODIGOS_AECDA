# Dado um vetor com tamanho n e um valor k a ser buscado
# • (a) Faça um pseudocódigo que determine se o valor k existe
# – seu programa deve retornar verdadeiro ou falso
# • (b) Implemente sua solução baseando-se apenas no seu pseudocódigo
# • (c) Faça a análise de complexidade do seu código

BuscarValor (v,n,k) 
for i = 0 in n:  #c1 n+1
  if v[1] == k: #c2 n
    return True #c3 0
return False    #c4 1

#T(n) = c1(n+1) + c2n + c4
#T(n) = c1n + c1 + c2n + c4 
#T(n) = (c1+c2)n + c1 + c4
#T(n) = an+b

