#Easy
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Assumptions: There can be negative ints. There can be duplicates. One solution. Not re-use of elements. 

# Hashmap solution. This should reduce the time complexity to O(n), but increase space complexity to n
def twoSumHash(intArray, sumTarget):
    #Step 1: Init lists and hash
    sumPairs = []
    hashTable = {}

    #Step 2: Get the second number by subtracting element from target
    for i,value in enumerate(intArray):
        secNum = sumTarget - value
        #Step 3: Look up second number in hash. If exists, you got a pair
        if secNum in hashTable: sumPairs.append([i,hashTable[secNum]])
        #Step 4: Insert currement element into the hash table
        hashTable[value] = i
    return sumPairs


#Solutions should be [[4, 3], [5, 3], [9, 0], [10, 1]]
print(twoSumHash([1,4,3,2,8,9-1,0,51,23,9,6], 10))

