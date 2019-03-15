d = {}
with open ('C:\\Users\\1\\Desktop\\meehmath_python\\rosalind\\protein_code.txt', 'r+') as text:
          for line in text:
                    line = line.strip().split()
                    if line[1] not in d:
                              d.update({line[1]: [line[0]]})
                    else:
                              
                              d[line[1]] += [line[0]]
protein = input('')
otvet = 1
for amino in protein:
          var = len(d.get(amino))
          otvet *= var
print((otvet*3)%1000000)

