import matplotlib.pyplot as plt

def calculatelength(sequence):
    total = len(sequence)
    return total

def reversecomplement(sequence):
    complement = ('A : T', "T : A", "C : G", "G : C")
    reverse = sequence[::-1]
    return f" 3'{reverse}5'"

def calculateGCvalues(sequence):
    total = len(sequence)
    GC = 0
    for i in range(len(sequence)):
        if sequence[i] == "G" or sequence[i] == "C":
           GC += 1
        else:
           continue
    return f"{GC / float(total) * 100}%"

def getnucleotides(sequence):
    nucleotides = {"A": 0, "T": 0, "C": 0, "G": 0}
    for i in sequence:
        if i in nucleotides:
            nucleotides[i] += 1
    return nucleotides

def DNAtoRNA(sequence):
    RNA = ""
    for i in range(len(sequence)):
        if sequence[i] == "T":
            RNA += "U"
        else:
            RNA += sequence[i]
    return RNA

def comparesequence(sequence1, sequence2):
    if sequence1 == sequence2:
        return "The sequences are the same"
    else:
        return "The sequences are not the same"


