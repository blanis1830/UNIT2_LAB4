# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE
#Blayne Hoy
#U2 Lab 4

def mat_sum(m1, m2):
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    return("No solution")

  result = [[0] * len(m1[0]) for _ in range(len(m1))]
  for a in range(len(m1)):
   for b in range(len(m2)):
    result[a][b] = m1[a][b] + m2[a][b] 
  return result

def mat_mul(m1, m2):
  if len(m1[0]) != len(m2):
    return("No solution")
  
  result = [[0] * len(m2[0]) for x in range(len(m1))]
  for c in range(len(m1)):
    for d in range(len(m2[0])):
      for e in range(len(m2)):
        result[c][d] += m1[c][e] * m2[e][d]
  return result


# [0,1]
# [1,0]
# [2.0]

# [0,1,2,3]
# [1,0,0,0]
