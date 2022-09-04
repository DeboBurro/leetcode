def aggregate_temp_change(temp):
    prefix_sum = [0] * len(temp)
    global_max_temp = float('-inf')
    for idx, val in enumerate(temp):
        if idx > 0:
            prefix_sum[idx] += temp[idx] + prefix_sum[idx-1]
        else:
            prefix_sum[idx] = temp[idx]
    for idx, val in enumerate(temp):
        global_max_temp = max(global_max_temp, prefix_sum[idx], prefix_sum[len(temp)-1] - prefix_sum[idx] + temp[idx])
    return global_max_temp


temp = [6, -2, 5]
# 6 4 9
print(aggregate_temp_change(temp))