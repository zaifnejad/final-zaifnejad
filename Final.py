import string
import re
def Find_Proteins(String, Dict):
    ReturnAA = ""

    for AminoAcid in Dict:
        if String in AminoAcid:
            ReturnAA += Dict[AminoAcid]
            return ReturnProtein

def Translation_Transcription(Sequence, Codon):
    ReturnDNA = []
    SanitizeTrans = Sequence.maketrans(string.ascii_lowercase, string.ascii_uppercase)
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

def Determine_Sequence():
    print("Please tell me the type of sequence you the file contains")
    FullSequence = input(
        "Press 1 for Codon\nPress 2 for Anti-Codon\nPress 3 for mRNA\nPress 4 for tRNA\nPress anything else to exit."
)
    return FullSequence

def Find_Start(SearchSequence):
    Slicer = 3
    StartSequence = ""
    SequenceList = []
    CutSequence = re.findall(r'AUG\w+', SearchSequence)
    StartSequence += CutSequence[0]
    for Characters in range(0, len(StartSequence), 3):
        SequenceList.append(StartSequence[Characters: Slicer])
        Slicer += 3
    return SequenceList

def Get_Sequence(File):
    with open(File, "r") as SequenceFile:
        ReturnFile = SequenceFile.readlines()
    return ReturnFile

def Sanitation(UnsanSequence):
    SanSequence1 = ""
    SanSequence1 = SanSequence1.join(UnsanSequence)
    SanSequence2 = SanSequence1.strip()
    FinalSanSequence = SanSequence2.replace(" ", "")
    return FinalSanSequence

def Create_New_File(EndAA):

def Main():
    fMET = "AUG"
    STOP = ("UAA", "UAG", "UGA")
    PHE = ("UUU", "UUC")
    LEU = ("UUA", "UUG", "CUA", "CUU", "CUC", "CUG")
    SER = ("UCU", "UCA", "UCG", "UCC", "AGU", "AGC")
    TYR = ("UAC", "UAU")
    CYS = ("UGU", "UGC")
    TRP = ("UGG")
    PRO = ("CCG", "CCA", "CCC", "CCU")
    HIS = ("CAU", "CAC")
    GLN = ("CAA", "CAG")
    ARG = ("CGG", "CGC", "CGA", "CGU", "AGA", "AGG")
    ILE = ("AUC", "AUA", "AUU")
    THR = ("ACC", "ACU", "ACA", "ACG")
    ASN = ("AAC", "AAU")
    LYS = ("AAA", "AAG")
    VAL = ("GUU", "GUA", "GUC", "GUG")
    ALA = ("GCU", "GCA", "GCC", "GCG")
    ASP = ("GAU", "GAC")
    GLU = ("GAA", "GAG")
    GLY = ("GGA", "GGC", "GGU", "GGG")

    AADict = {
        fMET: "MET",
        STOP: "Stop",
        PHE: "PHE",
        LEU: "LEU",
        SER: "SER",
        TYR: "TYR",
        CYS: "CYS",
        TRP: "TRP",
        PRO: "PRO",
        HIS: "HIS",
        GLN: "GLN",
        ARG: "ARG",
        ILE: "ILE",
        THR: "THR",
        ASN: "ASN",
        LYS: "LYS",
        VAL: "VAL",
        ALA: "ALA",
        ASP: "ASP",
        GLU: "GLU",
        GLY: "GLY"
    }
    while True:
        FileOpen = input("Please give me the name the .txt file with the DNA sequence:\n")
        try:
            MainSequence = Get_Sequence(FileOpen)
        except FileNotFoundError:
            print("The file name given can not be found.")
            continue
        break
    MainSequence = Sanitation(MainSequence)


if __name__ = "__main__":
    Main()
