class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPtr=0
        rightPtr=len(heights)-1
        maxWater=0

        while leftPtr!=rightPtr:
            if heights[leftPtr]>heights[rightPtr]:
                maxWater=max(maxWater, heights[rightPtr]*(rightPtr-leftPtr))
                rightPtr=rightPtr-1
            else:
                maxWater=max(maxWater, heights[leftPtr]*(rightPtr-leftPtr))
                leftPtr=leftPtr+1
        return maxWater

