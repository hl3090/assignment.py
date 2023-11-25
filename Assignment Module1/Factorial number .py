fact = lambda n: [1,0][n>0] or fact (n-1)*n
print (fact(5))