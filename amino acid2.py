
def translate(rslt): 
    table = { 
        'ATA':'ILEU-', 'ATC':'ILEU-', 'ATT':'ILEU-', 'ATG':'MET-', 
        'ACA':'THR-', 'ACC':'THR-', 'ACG':'THR-', 'ACT':'THR-', 
        'AAC':'ASN-', 'AAT':'ASN-', 'AAA':'LYS-', 'AAG':'LYS-', 
        'AGC':'SER-', 'AGT':'SER-', 'AGA':'ARG-', 'AGG':'ARG-',                  
        'CTA':'LEU-', 'CTC':'LEU-', 'CTG':'LEU-', 'CTT':'LEU-', 
        'CCA':'PRO-', 'CCC':'PRO-', 'CCG':'PRO-', 'CCT':'PRO-', 
        'CAC':'HIS-', 'CAT':'HIS-', 'CAA':'GLN-', 'CAG':'GLN-', 
        'CGA':'ARG-', 'CGC':'ARG-', 'CGG':'ARG-', 'CGT':'ARG-', 
        'GTA':'VAL-', 'GTC':'VAL-', 'GTG':'VAL-', 'GTT':'VAL-', 
        'GCA':'ALA-', 'GCC':'ALA-', 'GCG':'ALA-', 'GCT':'ALA-', 
        'GAC':'ASP-', 'GAT':'ASP-', 'GAA':'GLU-', 'GAG':'GLU-', 
        'GGA':'GLY-', 'GGC':'GLY-', 'GGG':'GLY-', 'GGT':'GLY-', 
        'TCA':'SER-', 'TCC':'SER-', 'TCG':'SER-', 'TCT':'SER-', 
        'TTC':'PHE-', 'TTT':'PHE-', 'TTA':'LEU-', 'TTG':'LEU-', 
        'TAC':'TYR-', 'TAT':'TYR-', 'TAA':'_', 'TAG':'_', 
        'TGC':'CYS-', 'TGT':'CYS-', 'TGA':'_', 'TGG':'TRY-', 

    } 
    protein ="" 
    sm = False

    for i in range(0, len(rslt)):

        codon = rslt[i:i + 3]


            if sm == True:
                if codon == ('TAA' or 'TAG' or 'TGA'):
                    return protein
                else: 
                    protein+= table[codon] 
            if codon ==('TTT' or 'TTC'):
                print('if you have 페닐케톤뇨증, 삼가 고인의 명복을 빔.')
    return False
             


print(translate())

            if protain"" in ('GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'MET', 'PHE', 'TRP', 'PRO'):
                 print('해당 폴리펩타이드가 아미노산 분자 내로 숨겨지는 구조입니다.')
            if protain"" in ('SER', 'THR', 'CYS', 'TYR', 'ASN', 'GLN', 'ASP', 'GLU', 'LYS','ARG','HIS'):
                 print('해당 폴리펩타이드가 아미노산 분자 표면으로 배치됩니다.)
   # 사슬모양, 고리형, 방향족 등의 특성도 넣기#         

