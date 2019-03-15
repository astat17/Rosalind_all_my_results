def control (number: int, a):
          for x in a:
                    if number==x:
                              return True
                    return False
def permutation (n: int, m: int = -1, prefix=None, k: int=0):
          m = n if m == -1 else m
          prefix = prefix or []
          if m==0:
                    print(prefix)
                    return
          for number in range(1,n+1):
                    if control(number, prefix):
                              continue
          prefix.append(number)
          k += 1
          permutation(n, m-1, prefix)
          prefix.pop()

permutation(3)          
