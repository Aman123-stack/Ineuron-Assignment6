









Q3>class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while(i<j):
            mid=i+(j-i)//2
            if(nums[mid]==target):
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l



Q4>class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        one,i=1,0
        while one:
            if i<len(digits):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    one=0
            else:
                digits.append(1)
                one=0
            i+=1
        return digits[::-1]







Q5>class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        num1copy=nums1[:m]
        p1=0
        p2=0
        p=0
        while(p<m+n):
            if(p2>=n or (p1<m and num1copy[p1]<nums2[p2])):
                nums1[p]=num1copy[p1]
                p1+=1
            else:
                nums1[p]=nums2[p2]
                p2+=1
            p+=1


Q6>class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        A=set()
        for n in nums:
            if n in A:
                return True
            A.add(n)
        return False


Q7> class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if(nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        return nums