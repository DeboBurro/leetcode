
# k  = 3
#         st      
#         end
#  1   3   2     3  5

def max_observable_sum_v2(stockPrice, k):
    if k < 1:
        return 0
    if not stockPrice:
        return 0
    cur_sum = stockPrice[0]
    max_sum = cur_sum
    st_idx = 0
    end_idx = 0
    memory = dict() # stockPrice : index
    memory[stockPrice[0]] = 0
    while end_idx + 1 != len(stockPrice):
        if stockPrice[end_idx + 1] in memory:
            if memory[stockPrice[end_idx+1]] == end_idx:
                memory = {stockPrice[end_idx+1]: end_idx+1}
                cur_sum = stockPrice[end_idx+1]
                st_idx = end_idx + 1
                end_idx = end_idx + 1
            else:
                while st_idx != memory[stockPrice[end_idx+1]] + 1:
                    cur_sum -= stockPrice[st_idx]
                    del memory[stockPrice[st_idx]]
                    st_idx += 1 
        else:
            if len(memory) < k:
                end_idx += 1
                cur_sum += stockPrice[end_idx]
                memory[stockPrice[end_idx]] = end_idx
            else:
                cur_sum -= stockPrice[st_idx]
                del memory[stockPrice[st_idx]]
                st_idx += 1

                end_idx += 1
                cur_sum += stockPrice[end_idx]
                memory[stockPrice[end_idx]] = end_idx
        if len(memory) == k:
            max_sum = max(max_sum, cur_sum)
            print(cur_sum)
    return max_sum
                


def max_observable_sum(stockPrice, k):
    if k < 1:
        return 0
    if not stockPrice:
        return 0
    cur_sum = stockPrice[0]
    max_sum = cur_sum
    st_idx = 0
    end_idx = 0
    memory = dict() # stock_price : index
    memory[stockPrice[0]] = 0
    while end_idx + 1 != len(stockPrice):
        if len(memory) < k:
            if stockPrice[end_idx+1] not in memory:
                end_idx += 1
                cur_sum += stockPrice[end_idx]
                memory[stockPrice[end_idx]] = end_idx
            else:
                while st_idx < memory[stockPrice[end_idx + 1]]:
                    cur_sum -= stockPrice[st_idx]
                    del memory[stockPrice[st_idx]]
                    st_idx += 1
                memory[stockPrice[end_idx + 1]] = st_idx
                end_idx += 1
                cur_sum += stockPrice[end_idx]
        else:
            cur_sum -= stockPrice[st_idx]
            del memory[stockPrice[st_idx]]
            st_idx += 1
        print(st_idx, end_idx, cur_sum)
        max_sum = max(max_sum, cur_sum)
    return max_sum


print(max_observable_sum_v2([1,2,7,7,4,3,6], 3))