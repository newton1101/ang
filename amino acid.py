
def comp(seq):  
    #상보적 방식 함수
    comp_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
=======
def comp(seq):  #상보적 방식 함수
    comp_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'} #상보적 관계 설정

    seq_comp=""
    for char in seq: #char는 2개 이상을 사용할 때 한 개의 문자열을 출력하게 하는 것
        if char in comp_dict: #char에 comp_dict가 없다면
            seq_comp = seq_comp + comp_dict[char] #추가하면 뒤에 추가
        else:
            seq_comp = seq_comp + '?' # 아니면 ? 추가
    return seq_comp
 
def rev(seq): #역순 방식 함수
    comp_dict={'A':'A', 'T':'T', 'C':'C', 'G':'G'}
    rev_str = "".join(reversed(seq)) # join은 리스트의 각 요소 사이에 특정 문자열을 붙여서 하나의 문자열로 반환하는 함수
    seq_rev = "" 
    for char in rev_str:  # char가 rev_str에 있으면
        if char in comp_dict:
            seq_rev = seq_rev + comp_dict[char] #추가
        else:
            seq_rev = seq_rev + '?' # ? 추가
    return seq_rev
 
def rev_comp(seq): #상보적 역순 방식 함수
    return (rev(comp(seq)))
 

src = input("DNA seq: ") #DNA 서열을 입력 받음
cnvt = int(input("1(Comp) 2(Rev) 3(Rev_Comp)")) #상보적 서열 과 역순과 역순의 상보적 

if cnvt == 1:
    rslt = comp(src)
elif cnvt == 2:
    rslt = rev(src)
else:
    rslt = rev_comp(src)
    
print(rslt)

    

