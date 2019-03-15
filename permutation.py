l=int(input(''))
input()
k=1
for i in range(1,l+1):
          k*=i
print(k)
def control (number, a):
          for x in a:
                    if number == x:
                              return True
          return False
def permutation (n: int, m: int = -1, prefix=None):
          m = n if m == -1 else m
          prefix = prefix or []
          if m==0:
                    print(*prefix)
                    return
          for number in range(1,n+1):
                    if control(number, prefix):
                              continue
                    prefix.append(number)
                    permutation(n, m-1, prefix)
                    prefix.pop()

permutation(l)     
