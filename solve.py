#partition array
from collections import Counter

def solve(k, nums):
    if k == 0 or len(nums) == 0:
        return "YES"
    if len(nums)%k != 0:
        return "NO"
    counter = Counter(nums)
    for entry in counter:
        if counter[entry] > len(nums)/k:
            return "NO"
    return "YES"


if __name__ == '__main__':
    print(solve(2,[1,2,3,4])) #yes
    print(solve(2,[1,2,3,3])) #yes
    print(solve(3,[1,2,3,4])) #no
    print(solve(3,[3,3,3,6,6,6,9,9,9]))#yes
    print(solve(1,[]))#yes
    print(solve(1,[1]))#yes
    print(solve(2,[1,2]))#yes