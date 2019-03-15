def isPalindrome (n:str, m:str):
          for i in range(len(n)//2):
                    if n[i] != m[len(n)-i-1]:
                              return False
          return True
                    
def replication (DNA:str):
          s = ''
          while len(DNA) != 0:
                    if DNA[0] == 'A':
                              s += 'T'
                    elif DNA[0] == 'T':
                              s += 'A'
                    elif DNA[0] == 'C' :
                              s += 'G'
                    elif DNA[0] == 'G':
                              s += 'C'
                    DNA = DNA[1:]
          return s
palindromes = []
positions = []
dna = input('')
dna_m = dna
dna_r = replication(dna)
for schet in range (len(dna)): #номер проверяемого нуклеотида
          if schet > 0:
                    dna_m, dna_r = dna_m[1:], dna_r[1:]
          for i in range (12,0, -1): #размер рамки 
                    if len(dna_m)<i:
                              continue
                    dna_mfr, dna_rfr = dna_m[:i], dna_r[:i]
                    if isPalindrome(dna_mfr, dna_rfr):
                              if 4 <= len(dna_mfr) <= 12 and len(dna_mfr)%2 == 0:
                                        palindromes.append(len(dna_mfr))
                                        positions.append(schet+1)
                                       
                                        
                                        

for i in range( len(positions)):
          print(positions[i], palindromes[i])
                              








                    
                    
                              
          
