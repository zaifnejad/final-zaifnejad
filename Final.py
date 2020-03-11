import string
import re
def Find_Proteins(String):
    fMET = "AUG"
    STOP = ["UAA", "UAG", "UGA"]
    PHE = ["UUU", "UUC"]
    LEU = ["UUA", "UUG", "CUA", "CUU", "CUC", "CUG"]
    SER = ["UCU", "UCA", "UCG", "UCC", "AGU", "AGC"]
    TYR = ["UAC", "UAU"]
    CYS = ["UGU", "UGC"]
    TRP = ["UGG"]
    PRO = ["CCG", "CCA", "CCC", "CCU"]
    HIS = ["CAU", "CAC"]
    GLN = ["CAA", "CAG"]
    ARG = ["CGG", "CGC", "CGA", "CGU", "AGA", "AGG"]
    ILE = ["AUC", "AUA", "AUU"]
    THR = ["ACC", "ACU", "ACA", "ACG"]
    ASN = ["AAC", "AAU"]
    LYS = ["AAA", "AAG"]
    VAL = ["GUU", "GUA", "GUC", "GUG"]
    ALA = ["GCU", "GCA", "GCC", "GCG"]
    ASP = ["GAU", "GAC"]
    GLU = ["GAA", "GAG"]
    GLY = ["GGA", "GGC", "GGU", "GGG"]

    ProteinsList = [fMET, STOP, PHE, LEU, SER, TYR, CYS, TRP, PRO, HIS, GLN, ARG, ILE, THR, ASN, LYS,, VAL, ALA, ASP, GLU, GLY]
    
    ReturnProtein = ""

    for Proteins in ProteinsList:
        for Protein in Proteins:
            if Protein == String:
                ReturnProtein += Protein
                return ReturnProtein

def Translation_Transcription(Sequence, Codon):
    ReturnDNA = []
    SanitizeTrans = Sequence.maketrans(string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
    Sanitize = Sequence.translate(SanitizeTrans)
    ReturnDNA.append(Sanitize)
    
    if Codon == 1: #Codon translation / transcription
        TemplateTrans = Sanitize.maketrans("ATCG", "TAGC")
        Template = Sanitize.translate(TemplateTrans)
        ReturnDNA.append(Template)
        mRNATrans = Sanitize.maketrans("ATCG", "UAGC")
        mRNA = Sanitize.translate(mRNATrans)
        ReturnDNA.append(mRNA)
        tRNATrans = mRNA.maketrans("AUCG", "UAGC")
        tRNA = mRNA.translate(tRNATrans)
        ReturnDNA.append(tRNA)
    elif Codon == 2: #Template translation / transcription
        CodonTrans = Sanitize.maketrans("ATCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        mRNATrans = CodonTemp.maketrans("ATCG", "UAGC")
        mRNA = CodonTemp.translate(mRNATrans)
        ReturnDNA.append(mRNA)
        tRNATrans = mRNA.maketrans("AUCG", "UAGC")
        tRNA = mRNA.translate(tRNATrans)
        ReturnDNA.append(tRNA)
    elif Codon == 3: #mRNA translation / transcription
        CodonTrans = Sanitize.maketrans("AUCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        TemplateTrans = CodonTemp.maketrans("ATCG", "TAGC")
        Template = CodonTemp.translate(TemplateTrans)
        ReturnDNA.append(Template)
        tRNATrans = Sanitize.maketrans("AUCG", "UAGC")
        tRNA = Sanitize.translate(mRNATrans)
        ReturnDNA.append(tRNA)
    elif Codon == 4: #tRNA translation / transcription
        CodonTrans = Sanitize.maketrans("AUCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        TemplateTrans = CodonTemp.maketrans("ATCG", "TAGC")
        Template = CodonTemp.translate(TemplateTrans)
        ReturnDNA.append(Template)
        mRNATrans = Sanitize.maketrans("AUCG", "UAGC")
        mRNA = Sanitize.translate(mRNATrans)
        ReturnDNA.append(mRNA)
    return ReturnDNA

    
if __name__ = "__main__":
    Main()
