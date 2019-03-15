d={}
with open  ('C:\\Users\\1\\Desktop\\meehmath_python\\rosalind\\protein_code.txt', 'r') as text:
          for line in text:
                    line = line.strip().split(' ')
                    d.update({line[0]:line[1]})
dna = input('')
def transcription (DNA: str):
          s, dlina='', len(DNA)
          for k in range(dlina):
                    if DNA[0] == 'T':
                              s += 'U'
                    else:
                              s += DNA[0] 
                    DNA = DNA[1:]
          return s

RNA = transcription(dna)       
RNA_f,frame, protein, = '', '', '' 

for i in range (4):
          frame = RNA[i:]
          c = True
          while c:
                    for k in range(0, len(frame), 3):
                              if frame[k : k+3] == 'AUG':
                                        RNA_f = frame[k:]
                                        print(RNA_f)
                                        c = False
                    
          for k in range(len(RNA_f)):
                    amc = RNA_f[k : k+3]
                    if d[amc] == 'Stop':
                              break
                    protein += d[amc]
                    
                    
          print(protein)
                              
                    
                              

                    
