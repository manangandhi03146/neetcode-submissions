class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr=0
        rightPtr=len(numbers)-1
        result=[0]*2

        while leftPtr<rightPtr:
            if (numbers[leftPtr]+numbers[rightPtr])==target:
                result[0]=leftPtr+1
                result[1]=rightPtr+1
                return result

            elif (numbers[leftPtr]+numbers[rightPtr])<target:
                leftPtr+=1
            
            else:
                rightPtr-=1