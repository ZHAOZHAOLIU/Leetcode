#---Author: ZHAOZHAO LIU
#---Version:1.0
#---Date:27-09-2020
#考点：
#1.用Stack来进行查找，stack的特性是后进先出。push()/pop()/get_top()
#2.Stack可以直接使用Python中list的特性，list.append(),list.pop()

#implement：
#1.如果是左侧符号就压入list中，如果是右侧符号，就去list中比较最后一个元素与符号是否成对
#2.如果list为空，而符号还有，那就说明不匹配
#3.如果最后list不为空，也说明不匹配

#注意事项：
#1.时刻注意list为空的情况，可能只输入一个字符。

#时间复杂度：O(n)
#空间复杂度：O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        match_find={"]":"[","}":"{",")":"("}
        l=[]
        for i in s:
            if i in {"]",")","}"}:
                if len(l)>0 :
                    if l[-1]==match_find[i]:
                        l.pop()
                    else:
                        return False
                else:
                    return False
            else:
                l.append(i)
        if len(l)<1:
            return True
        else:
            return False