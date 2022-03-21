class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i_s = 0
        i_p = 0
        N_p = len(p)
        N_s = len(s)

        while (N_p <= N_s):
            cur = s[i_s]

            if not p[i_p] == '*':
                p_eff = p[i_p]

            if cur == p[i_p] or p[i_p] == '.':
                if (i_p < N_p -1):
                    i_p += 1
                    i_s += 1
                elif (i_s == N_s-1):
                    return True
                else: return False

            elif p[i_p] == '*':
                if p_eff == s[i_s] or p_eff == '.':
                    i_s += 1
                elif i_p < N_p -1 :
                    i_p += 1
                else:
                    return False 
            else:
                return False

            if i_s == N_s:
                return True
        
        while (N_p > N_s):
            cur = s[i_s] 

            if (not p[i_p] == '*'):
                p_eff = p[i_p]

            if cur == p[i_p] or p[i_p] == '.':
                if (i_s <= N_s -1):
                    i_p += 1
                    i_s += 1
                elif (i_p == N_p-1):
                    return True

                else: return False

            elif p[i_p] == '*':
                if p_eff == s[i_s] or p_eff == '.':
                    i_s += 1
                else:
                    i_p += 1

            else:return False

            if i_p == N_p:
                return True

            
