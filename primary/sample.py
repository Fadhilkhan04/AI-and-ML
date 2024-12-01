import numpy as np

#ques1
print("\nCREATE ARRAY")
print("\n")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


#ques3
print("\nFILL ZEROES")
print("\n")
arr1 = np.zeros((5))
print(arr1)


#ques4
print("\nFILL ONES")
print("\n")
array = np.ones(5) 
print(array)


#ques5
print("\nRESHAPE")
print("\n")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr3 = arr2.reshape(4, 2)
print ('After reshaping having dimension 4x2:')
print (arr3)
print ('\n')

#ques6
print("\nTRANSPOSE")
print("\n")
beforetranspose = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
 
# before transpose
print(beforetranspose, end ='\n\n')
 
# after transpose
print(beforetranspose.transpose())


#ques7
print("\nMULTIPLY")
print("\n")
in_num1 = 4
in_num2 = 6

out_num = np.multiply(in_num1, in_num2)  
print ("output number : ", out_num)


#ques8
print("\nOPERATION")
print("\n")

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d[0][0])
print(arr_2d[0])
print(arr_2d[:,1])


#ques9
print("\nGENERATE")
print("\n")
rand = np.random.randint(10, size=(2, 2)) 
print(rand)