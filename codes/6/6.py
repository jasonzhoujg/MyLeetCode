class Solution:
    def convert(self, s: str, numRows: int) -> str:
      
        if numRows==1:return s
        row_set = ["" for i in range(numRows)]
        cnt = 0
        res = ""
        while cnt <len(s):
            for i in range(numRows):
                if cnt <len(s): 
                    row_set[i]+=s[cnt]
                    cnt+=1
                else:
                    for j in range(numRows):
                        res += row_set[j]
                    return res
            if numRows>2:       
                for i in range(numRows-2):
                    if cnt <len(s): 
                        row_set[numRows-2-i]+=s[cnt]
                        cnt+=1
                    else:
                        for j in range(numRows):
                            res += row_set[j]
                        return res

        for j in range(numRows):
            res += row_set[j]
        return res
