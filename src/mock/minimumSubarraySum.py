"""
    [3,1,2] => [3], [1], [2], [3,1], [1,2], [3,1,2]
                3 +  1  + 2  +  1  +   1  +    1   = 9

array : counld be empty
positive integers

                |
ex: [  5  3 1  2 4 ]
5  53  531   5312    53124  |   3  31 312  3124   |  1   12  124  |  2 24   |  4    
 
5  3    1      1       1        3   1  1   1         1   1    1      2  2      4

smaller : [  ]
     val: ind
  
     2 : 3
     1 : 2 
    stack

To the right, next idx smaller than itself
              [ 1,  2,  5, 5,  5 ]
To the left, next idx smaller than itself
              [ -1  -1  -1  2  3  ]
        5 : idx = 0
     5 * (1 - 0) * (0 - (-1)) = 5
        3 : idx = 1
     3 * (2 -1 ) * (1 - (-1))  = 6
        1 : idx = 2
     1 * (5 - 2) * (2 - (-1)) = 9
        2 : idx = 3
     2 * ( 5 - 3) * (3 - 2) = 4
        4 : idx = 4
     4 * (5 - 4) * (4 - 3) = 4

     5 + 6 + 9 + 4 + 4 = 28

"""

# Solution 1 : brutal force
# TC: O(n^3)
# Space C : O(1)
# def min_subarrary_sum(arr):
#     summation = 0
#     if not arr:
#         return summation
#     for st_idx, val in enumerate(arr):
#         for end_idx in range(len(arr)-1, st_idx-1, -1):
#             summation += min(arr[st_idx:end_idx+1])
#     return summation
# arr = [3,1,2]
# print(min_subarrary_sum(arr))


# Solution 2:
# TC : O(n)
# space : O(n)

def min_subarrary_sum_optimal(arr):
    if not arr:
        return 0
    # 1. create two monotonic stacks that identifies which indices are smaller than you ( those are your boundaries)
    left_mono =   [ -1 ] * len(arr)
    right_mono =  [ len(arr) ] * len(arr) 
    inc_stack = []
    dec_stack = []
    summation = 0 
    for idx, val in enumerate(arr):
        if not inc_stack:
            inc_stack.append((idx, val))
        # creating a increasing monotonic stack
        if inc_stack and inc_stack[-1][1] > val:
            pre_idx, pre_val = inc_stack.pop()
            inc_stack.append((idx, val))
            right_mono[pre_idx] = idx

    for idx, val in enumerate(arr[::-1]):
        idx = len(arr) - 1 - idx
        if not dec_stack:
            dec_stack.append((idx, val))
        # creating a decreasing monotonic stack
        elif dec_stack and dec_stack[-1][1] > val:
            pre_idx, pre_val = dec_stack.pop()
            dec_stack.append((idx, val))
            left_mono[pre_idx] = idx
    print(f'right mono = { right_mono  }')
    print(f'left mono = { left_mono  }')

    # 2. Use each index of the items to be pivot and calculate the contribution each pivot can contribute to
    for idx, val in enumerate(arr):
        summation += val * (right_mono[idx] - idx) * (idx - left_mono[idx])
        print(f'{val} * {right_mono[idx] - idx} * {idx - left_mono[idx]}')
    return summation

# arr = [5,3,1,2,4]
arr = [11,81,94,43,3]

# 11 * 4 + 81 * 2 + 94 + 43 *3 + 3 *5 

print(min_subarrary_sum_optimal(arr))