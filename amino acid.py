def comp(seq):  
    #상보적 방식 함수
    comp_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    seq_comp=""
    for char in seq:
        if char in comp_dict:
            seq_comp = seq_comp + comp_dict[char]
        else:
            seq_comp = seq_comp + '?'
    return seq_comp
 
def rev(seq): #역순 방식 함수
    comp_dict={'A':'A', 'T':'T', 'C':'C', 'G':'G'}
    rev_str = "".join(reversed(seq))
    seq_rev = ""
    for char in rev_str:
        if char in comp_dict:
            seq_rev = seq_rev + comp_dict[char]
        else:
            seq_rev = seq_rev + '?'
    return seq_rev
 
def rev_comp(seq): #상보적 역순 방식 함수
    return (rev(comp(seq)))
 

src = input("DNA seq: ")
cnvt = int(input("1(Comp) 2(Rev) 3(Rev_Comp)"))

if cnvt == 1:
    rslt = comp(src)
elif cnvt == 2:
    rslt = rev(src)
else:
    rslt = rev_comp(src)
    
print(rslt)

    

