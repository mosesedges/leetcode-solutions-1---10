def TwoSums(num:list[int], target:int)-> list[int]:
  hashmap = {}
  for i,n in enumerate(num):
    diff = taget - n
    if diff in hashmap:
      return hashmap[diff], i
    hashmap[n] = i
