q1>def reconstructPermutation(s):
    perm = []
    n = len(s)
    low, high = 0, n

    for ch in s:
        if ch == 'I':
            perm.append(low)
            low += 1
        elif ch == 'D':
            perm.append(high)
            high -= 1

    # Append the remaining element
    perm.append(low)

    return perm
q2>def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
q3>def validMountainArray(arr):
    if len(arr) < 3:
        return False

    n = len(arr)
    left, right = 0, n - 1

    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1

    if left == right or left == 0 or right == n - 1:
        return False

    return True
q4>def findMaxLength(nums):
    max_len = 0
    count = 0
    count_map = {0: -1}

    for i in range(len(nums)):
        count += 1 if nums[i] == 0 else -1

        if count == 0:
            max_len = i + 1
        elif count in count_map:
            length = i - count_map[count]
            if length > max_len:
                max_len = length
        else:
            count_map[count] = i

    return max_len
q5>def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort()
    n = len(nums1)
    min_product_sum = 0

    for i in range(n):
        min_product_sum += nums1[i] * nums2[n - i - 1]

    return min_product_sum
q6>from collections import defaultdict

def findOriginalArray(changed):
    count = defaultdict(int)

    for num in changed:
        count[num] += 1
        if num % 2 == 0 and count[num // 2] > 0:
            count[num // 2] -= 1
        elif num % 2 != 0:
            return []

    original = []

    for num in changed:
        while count[num] > 0:
            original.append(num // 2)
            count[num] -= 1

    return original
q7>from collections import defaultdict

def findOriginalArray(changed):
    count = defaultdict(int)

    for num in changed:
        count[num] += 1
        if num % 2 == 0 and count[num // 2] > 0:
            count[num // 2] -= 1
        elif num % 2 != 0:
            return []

    original = []

    for num in changed:
        while count[num] > 0:
            original.append(num // 2)
            count[num] -= 1

    return original
q8>def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += mat1[i][p] * mat2[p][j]

    return result
