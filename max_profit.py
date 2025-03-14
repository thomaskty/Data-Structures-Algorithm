

def max_profit(nums):
    B = nums[0] 
    maxprofit = 0
    for i in range(0,len(nums)):
        if nums[i]<B:
            B = nums[i]

        profit = nums[i]-B
        if profit>maxprofit:
            maxprofit = profit
            
        # print(i,B,profit,maxprofit) 
    return maxprofit  

nums = [1,2]
max_profit(nums)

