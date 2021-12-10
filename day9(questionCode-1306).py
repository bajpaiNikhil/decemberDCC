def canReach(A, i):
    if 0 <= i < len(A) and A[i] >= 0:
        A[i] = -A[i]
        return A[i] == 0 or canReach(A, i + A[i]) or canReach(A, i - A[i])
    return False

A = [4,2,3,0,3,1,2]
start = 5




print(canReach(A,start))