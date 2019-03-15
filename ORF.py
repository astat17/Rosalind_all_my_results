d={}
with open  ('C:\\Users\\1\\Desktop\\meehmath_python\\rosalind\\protein_code.txt', 'r') as text:
          for line in text:
                    line = line.strip().split(' ')
                    d.update({line[0]:line[1]})
dna = input('')
def replication (DNA:str):
          s = ' '
          while len(DNA) != 0:
                    if DNA[-1] == 'A':
                              s += 'T'
                    elif DNA[-1] == 'T':
                              s += 'A'
                    elif DNA[-1] == 'C' :
                              s += 'G'
                    elif DNA[-1] == 'G':
                              s += 'C'
                    DNA = DNA[:-1]
          return s
def transcription (DNA: str):
          s, dlina='', len(DNA)
          for k in range(dlina):
                    if DNA[0] == 'T':
                              s += 'U'
                    else:
                              s+=DNA[0]
                    DNA = DNA[1:]
          return s
rna_r = replication(dna)
rna_rr = transcription(rna_r)
rna = transcription (dna)
protein = ''
for  i in range(0,3):
          rna_m = rna_rr[i:]
          for k in range(0, len(rna_m), 3):
                              if rna_m[k : k+3] == 'AUG':
                                        result = rna_m[k:]
                                        print(result)
                                        break


          for k in range(0,len(result), 3):
                    amc = result[k : k+3] 
                    if d[amc] == 'Stop':
                              print('qeq')
                              break
                    
                    else:
                              protein += d[amc]
                              
print(protein)
          










          
