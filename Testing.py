'''
i=10.87 
print(type(i))
j=int(i)
print(type(j),i)


import sys

if len(sys.argv)==2:
    print("You might be give two argumernts")
    sys.exit()
fullname=sys.argv[1:]
print ("Length is: ",len(fullname))

strg=" ".join(fullname)
print(strg)

email=strg.lower().replace(" ",".")+"@gmail.com"

print("fullname:",fullname)
print("email:",email)



strg="world"
print(strg[:2]) # wo
print(strg[2:]) # ld
print(strg[:-1])#worl
print(strg[-3:])# rld
print(strg[-3:-1]) #rl
print(strg[2:-1]) #rl
print(strg[2:4]) #rl
'''
from Tools.scripts.generate_re_casefix import alpha

'''
strg="This the id : uxwe123. please react"
res=strg.split(':')[1].split('.')[0].strip()
print(res)


off="This is your kind msg Np100 cupon"
if 'Np100' in off:
    print("offer valis")

print(off.find("Np100"))


name="Abinesh Rajendran"
lis= ''.join([word[0].upper() for word in name.split()])
print(lis)

r=0
count=sum([len(word) for word in name.split()])
print(count)

data=[1,2,3,4,5]
sam=(data for i in data if i==3)
print(sam)


msg="This the id ::: uxwe123. please react"
print(msg.split(':')) #['This the id ', '', '', ' uxwe123. please react']
'''
'''
for i in range(5):
    print(i)
else:
    print("End")
'''
'''

class sample:
    def __init__(name,name,reg):
       # self1.n=name Error
        name.name=name
        name.r=reg

    def prints(self2):
        print(f"{self2.n} is {self2.r}")

s=sample('Abinesh',2021)
s.prints()

'''




#*******************************//LEETCODE//*********************************************
#TWO SUM
'''

def find_tar(nums,tar):
    hash_map={}
    for index,value in enumerate(nums):
        val=tar-value
        if value in hash_map:
            return [hash_map[value],index]
        hash_map[val]=index
    return None


lis=[3,3]
target=6
print(find_tar(lis,target))
'''


#Contain Duplicate
'''
class Solution:
    def contains(self,nums):
        num=[]
        for i in nums:
            if i in num:
                return True
            num.append(i)
        if len(num)==len(nums):
            return False

ob=Solution()
nums = [1,2,3,5,3]
print(ob.contains(nums))
'''
#Valid Anagram
#Method 1
'''
class Solution:
    def isAnagram(self,stg,tar):
        count={}
        for letter in stg:
            if letter not in count:
                count[letter]=1
            else:
                count[letter]+=1
        for letter in tar:
            if letter not in count:
                return False
            else:
                if count[letter]==1:
                    del count[letter]
                else:
                    count[letter]-=1
        if count=={}:
            return True
        else:
            return False

obj=Solution()
s1="anagram"
s2="nagrram"
print(obj.isAnagram(s1,s2))

'''

#METHOD 2
'''
class Solution:
    def isAnagram(self,stg,tar):
        if len(stg)!=len(tar):
            return False
        count_stg={}
        count_tar={}
        for i in range(len(stg)) :
            count_stg[stg[i]] = count_stg.get(stg[i],0) + 1
            count_tar[tar[i]] = count_tar.get(tar[i], 0) + 1
        for letter in stg:
            if count_stg[letter]!=count_tar.get(letter,0):
                return False

        return True

obj=Solution()
s1="anagram"
s2="nagaram"
print(obj.isAnagram(s1,s2))
'''
'''
#######// GROUP ANAGRAM //########
class Solution:
    def groupanagram(self,strs):
        hash={}
        for st in strs:
            l="".join(sorted(st))
            if l in hash:
                hash[l].append(st)
            else:
                hash[l]=[st]

        return list(hash.values())
obj=Solution()
s1=["eat","tea","tan","ate","nat","bat"]
print(obj.groupanagram(s1))

'''

'''
#######// Top K Frequent Element //########
class Solution(object):
    def topKFrequent(self, nums, k):

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        res=[]
        for v,f in count.items():
            bucket[f].append(v)
        for val in range(len(bucket)-1,0,-1):
            for i in bucket[val]:
                res.append(i)
                if len(res)==k:
                    return res
obj=Solution()
s1=[1,1,1,2,2,3]
k = 2
print(obj.topKFrequent(s1,k))

'''
#######// Valid Palindrome //########
'''
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        new_s=""
        for i in s:
            if  i.isalnum():
                new_s+=i
        l=0
        r=len(new_s)-1
        print(new_s)
        while l<r:
            if new_s[l]!=new_s[r]:
                return False
            else:
                l+=1
                r-=1

        return True

obj = Solution()
s1 = "0p"
print(obj.isPalindrome(s1))

'''

#############// TWO POINTER //#################
# Two pointers mostly used in sorted array
#TWO SUM Example
class Solution:
    def twopointer(self,nums,t):
        l=0
        r=len(nums)-1
        while l<r:
            val=nums[l]+nums[r]
            if val==t:
                return [l,r]
            elif val<t:
                l+=1
            elif val>t:
                r-=1

        return "No match"

obj = Solution()
s1 = [1,2,3,4,5,6]
t=5
print(obj.twopointer(s1,t))