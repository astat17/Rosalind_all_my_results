DNA, motif = input(), input()
DNA_sr = None
m = len(motif)
indexes = []
for i in range (len(DNA)):
          DNA_sr = DNA[i:m+i]
          if DNA_sr == motif:
                    indexes.append(i+1)
print(*indexes)
          
          
