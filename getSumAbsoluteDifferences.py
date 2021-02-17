def getSumAbsoluteDifferences(nums):
    sum_fwd = [0]
    sum_bwd = [0]
    for ind in range(len(nums)):
        sum_fwd.append(sum_fwd[-1] + nums[ind])
        sum_bwd.append(sum_bwd[-1] + nums[len(nums)-1-ind])
        print("sum_fwd: ", sum_fwd)
        print("sum_bwd: ", sum_bwd)
    answer = []
    for i in range(len(nums)):
        answer.append((2*i-len(nums))*nums[i] - sum_fwd[i] + sum_bwd[-i-1])
    return answer

n = [2, 3, 5]
print(getSumAbsoluteDifferences(n))