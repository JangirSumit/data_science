# 8. With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   
# write   a program to make a list whose elements are intersection of the above given lists.

listA = [1,3,6,78,35,55] 
listB = [12,24,35,24,88,120,155]

setA = set(listA)
setB = set(listB)

insersaction_of_AB = setA.intersection(setB) #A&B
listA_insersact_B = list(insersaction_of_AB)

print(listA_insersact_B)
