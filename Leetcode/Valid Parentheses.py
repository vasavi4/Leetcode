class Solution:
    def isValid(self, s: str) -> bool:
        o="({["
        c=")}]"
        st=[]
        for i in s:
            if i in c and len(st)==0:
                return False
            if i in o:
                st.append(i)
            elif i in c:
                if i==")" and st[-1]!="(":
                    return False
                if i=="}" and st[-1]!="{":
                    return False
                if i=="]" and st[-1]!="[":
                    return False
                else:
                    st.pop()
        if len(st)==0:
            return True        
