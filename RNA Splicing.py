my_set = []
with open ('C:\\Users\\1\\Downloads\\rosalind_splc1.txt ') as text:
          for line in text:
                    line = line.strip()#.split('/n')
                    my_set.append(line)

my_set = my_set[1:]
DNA = ''
for i in range(len(my_set)):
          if my_set[i].isupper():
                    DNA += my_set[i]
          else:
                    break
print(DNA)
for i in range(len(my_set)):
          if not my_set[i].isupper():
                    my_set = my_set[i:]
                    break
                    
print(my_set)
for i in range(1, len(my_set)+1, 2):
          exon = DNA.replace(my_set[i], ' ')
          DNA = exon
exon = exon.split(' ')
mDNA = exon[0]
for i in range(1, len(exon)):
          mDNA += exon[i]

d, RNA={}, ''
for i in range(len(mDNA)):
          if mDNA[i] == 'T':
                    RNA += 'U'
          else:
                    RNA += mDNA[i]
with open ('C:\\Users\\1\\Desktop\\meehmath_python\\rosalind\\protein_code.txt', 'r+') as code:
          for el in code:
                    el = el.strip().split(' ')
                    d.update({el[0]:el[1]})
print(d)                 
protein = ''
for k in range(0, len(RNA), 3):
          protein += str(d.get(RNA[k:k+3]))
          
print(protein[:-4])
          

          


                    
