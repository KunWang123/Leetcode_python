题目描述：
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2

思路：
现在我们重排这个数组，从头到尾依次扫描这个数组中的每个数字。当扫描到下标是i的数字时，首先比较这个数字（用m表示）是不是等于i。
如果是，则扫描下一个数字；如果不是，则拿它和第m个数字惊醒比较。如果它和第m个数字相等，就找到了一个重复的数字（改数字在下标为i和m的位置都出现了）；
如果它和第m个数字不相等，就把第i个数字和第m个数字交换，把m放到属于他的位置，接下来重复这个比较、交换的过程，直到发现一重复的数字。

实现：
python
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) <= 0:
            return False
        for i in range(len(numbers)):
            if numbers[i] >= len(numbers) or numbers[i] < 0:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    tmp = numbers[numbers[i]]
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = tmp
        return False
        
值得思考：
1、假设找出数组中全部重复的数字，（应将重复的数字加入set()，一次类推）
2、如果找到数字并输出重复几次（待思考）
3、如果取消数字的限制，数字不只是在0~n-1之间（待思考）
