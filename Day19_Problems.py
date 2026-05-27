
#Roman to Integer

class Solution:
    def romanToInt(self,s:str) -> int:
        roman={
            'I':1, 'V':5, 'X':10 , 'L':50,
            'C':100 , 'D':500,'M':1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total

s = input('Enter a roman number: ')
RomanToInt = Solution()
Result = RomanToInt.romanToInt(s)
print(Result)

#Two sum
nums = [3,2,4]
target = 6
class Solve:
    def TwoSum(self, nums:list[int], target = int) ->list[int]:
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[j] == target - nums[i] :
                    return [i,j]
        return []
                
sol = Solve()
result = sol.TwoSum(nums,target)
print(result)



