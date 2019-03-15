d={}
with open ('C:\\Users\\1\\Desktop\\meehmath_python\\rosalind\\protein_code.txt', 'r+') as code:
          for line in code:
                    line = line.strip().split(' ')
                    d.update({line[0]:line[1]})
                    
RNA = input('')
protein = ''
for i in range(0, len(RNA), 3):
          protein += d.get(RNA[i:i+3])
          
print(protein[:-4])
