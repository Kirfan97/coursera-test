
nums= [3,2,4]
target = 6


def twoSum( nums, target):
     s=set()
     print(s)
     for i in range(len(nums)):
          print(target)
          print(nums[i])
          if target-nums[i] in s:
              
               print(s)
               return [i,nums.index(target-nums[i])]
          else:
               s.add(nums[i])
     
               

print(twoSum(nums,target))