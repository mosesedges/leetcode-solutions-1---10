def TwoSums(num:list[int], target:int)-> list[int]:
  hashmap = {}
  for i,n in enumerate(num):
    diff = taget - n
    if diff in hashmap:
      return print(hashmap[diff], i)
    hashmap[n] = i
TwoSum([2,3,5,7,12], 9)
