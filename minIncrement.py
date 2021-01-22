def minIncrementForUnique(A):
        """
        :type A: List[int]
        :rtype: int
        """       
        n = len(A)
        if n < 0:
            return 0
        if n == 2:
            if A[0] == A[1]:
                return 1
        else:
            A.sort()
            count = 0 
            p = 1
            while p < n:
                #print(n)
                if A[p] <= A[p-1]:
                    count += A[p-1] - A[p] + 1
                    A[p] = A[p-1] + 1
                p += 1
            return count
            
print(minIncrementForUnique([3,2,1,2,1,7]))