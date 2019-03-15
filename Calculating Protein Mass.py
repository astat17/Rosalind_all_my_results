d={}
with open ('C:\\Users\\1\\Desktop\\meehmath_python\\rosalind\\aminoacid_mass.txt', 'r+') as text:
          for line in text:
                    line = line.strip().split()        
                    d.update({line[0]:float(line[1])})
protein = input('')
mass = 0
for acid in protein:
           mass += d.get(acid)
print(round(mass, 3))
          
