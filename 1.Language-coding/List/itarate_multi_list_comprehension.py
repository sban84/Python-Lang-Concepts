


l1 = [1,2,3,4]
l2 = ["a","b","c","d"]
l3 = [1.00,2.00,3.00]


r  = [ (i,j ) for (i,j) in zip(l1,l2 ) ]
print(r)


r  = [ (i,j , k) for (i,j,k) in zip(l1,l2 , l3) ]
print(r)