class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=""
        st=[]
        o="({["
        for i in s:
            if i in o:
                st.append(i)
                if len(st)==1:
                    continue
                else:
                    if i=="(":
                        a=a+"("
                    if i=="{":
                        a=a+"{"
                    if i=="[":
                        a=a+"["
            else:
                if i==")" and len(st)>1:
                    st.pop()
                    a=a+")"
                elif i=="}" and len(st)>1:
                    st.pop()
                    a=a+"}"
                elif i=="]" and len(st)>1:
                    st.pop()
                    a=a+"]"
                else:
                    st.pop()
        return a            
