dnas, m = ['' for i in range(500)], 0
with open ('C:\\Users\\1\\Downloads\\rosalind_cons.txt', 'r+') as text:
          for line in text:
                    line = line.strip()
                    if line.isupper():
                              dnas[m] += str(line)
                    else:
                              m+=1
          
dnas = dnas[1:m+1]

i, k = 0, 0
A, C, G, T = [0 for i in range(len(dnas[0]))], [0 for i in range(len(dnas[0]))], [0 for i in range(len(dnas[0]))], [0 for i in range(len(dnas[0]))]
while i!=len(dnas[0]):
          for dna in dnas:
                    if dna[i] == 'A':
                              A[i]+=1
                    elif dna[i] == 'C':
                              C[i]+=1
                    elif dna[i] == 'G':
                              G[i]+=1
                    elif dna[i] == 'T':
                              T[i]+=1
          i+=1
consensus = ''
while k!=len(dnas[0]):
          a = max(A[k], C[k], G[k], T[k])
          if A[k] == a:
                    consensus += 'A'
                    k+=1
                    
          elif C[k] == a:
                    consensus += 'C'
                    k+=1
                    
          elif G[k] == a:
                    consensus += 'G'
                    k+=1
                    
          
          elif T[k] == a:
                    consensus += 'T'
                    k+=1
                    
          

print(consensus)
nuc, alln = ['A', 'C', 'G', 'T'], [A, C, G, T]
for i in range(4):
          print(str(nuc[i])+':', *alln[i])
                    
          
          
                    

                    
