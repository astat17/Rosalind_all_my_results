first_dna, second_dna, mutation = input(''), input(''), 0
for i in range ( len (first_dna) ):
          if first_dna[i] != second_dna[i]:
                    mutation += 1
print(mutation)
