DNA = input(' ')

DNA2 = DNA #for the second version 

s = ''
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
print(s)


def second_version (dna:str, complement = ''):
          dna = dna[::-1]
          for i in range(len(dna)):
                    if dna[i] == 'A':
                              complement += 'T'
                    elif dna[i] == 'T':
                              complement += 'A'
                    elif dna[i] == 'C' :
                              complement += 'G'
                    elif dna[i] == 'G':
                              complement += 'C'
          return complement
print(second_version(DNA2))
                    


          
                    
          
