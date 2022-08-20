def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    # ascii: 65~90 (대문자) / 97~122 (소문자)
    lst1, lst2 = [], []
    for i in range(len(str1)-1):
        if 65<=ord(str1[i])<=90 and 65<=ord(str1[i+1])<=90:
            lst1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if 65<=ord(str2[i])<=90 and 65<=ord(str2[i+1])<=90:
            lst2.append(str2[i]+str2[i+1])
    
    lst1_copy = lst1.copy()
    lst2_copy = lst2.copy()
    intersection, union = 0, 0
    for i in lst1_copy:
        if i in lst2_copy:
            lst2_copy.remove(i)
            intersection += 1
    
    lst1_copy = lst1.copy()
    lst2_copy = lst2.copy()
    for i in lst1_copy:
        if i in lst2_copy:
            lst2_copy.remove(i)
        union += 1
    union += (len(lst1_copy) - union + len(lst2_copy))
    
    if union == 0 and intersection == 0:
        answer = 65536
    else:
        answer = ((intersection / union) * 65536) // 1
        
    return answer