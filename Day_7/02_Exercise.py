# 1.- JOin A and B.
A = {2, 4, 6, 8, 10, 12}
B = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#-------------------------------------------------------------------------------------
# 2.- Find intersection.
C = A.union(B)
print(C)
#-------------------------------------------------------------------------------------
# 3.- Is A subset of B.
print(A.intersection(B))
#-------------------------------------------------------------------------------------
# 4.- Are A and B disjoint sets.
print(A.isdisjoint(B))
#-------------------------------------------------------------------------------------
# 5.- Join A with B and B with A.
AB = A.union(B)
BA = B.union(A)
print(AB,BA)
#-------------------------------------------------------------------------------------
# 6.- What is the symmetric difference between A and B.
print(A.symmetric_difference(B))
#-------------------------------------------------------------------------------------
# 7.- Del A and B.
del A,B