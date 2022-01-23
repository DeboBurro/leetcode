class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # Approach 1 : prefix sum 
        if time == 0: return [i for i in range(len(security))]
        res = []
        nonInc = [0]
        nonDec = [0]
        revSecurity = security[::-1]
        for i in range(1, len(security)):
            if security[i-1] >= security[i]:
                nonInc.append(nonInc[-1] + 1)
            else:
                nonInc.append(0)
            if revSecurity[i-1] >= revSecurity[i]:
                nonDec.append(nonDec[-1] + 1)
            else:
                nonDec.append(0)
        nonDec = nonDec[::-1]
        for i in range(len(security)):
            if nonInc[i]  >= time and nonDec[i] >= time:
                res.append(i)
        return res
