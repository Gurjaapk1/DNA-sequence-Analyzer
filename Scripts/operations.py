import os
from Bio import SeqIO
import matplotlib.pyplot as plt
from .DNAsequenceanalyzer import (calculateGCvalues,
getnucleotides, reversecomplement, calculatelength, DNAtoRNA)
from .Graphs import (plotnucleotidefrequency, plotGCcontent,
ScatterplotGC_vs_lenght, Heatmap)

def readfastafile(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    with open(filename, "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            return seq_record.seq

def writeoutput(filepath, data, inputfile):
    sequence = data[0]
    gc_content = calculateGCvalues(sequence)
    nucleotides = getnucleotides(sequence)
    reverse = reversecomplement(sequence)
    length = calculatelength(sequence)
    rna = DNAtoRNA(sequence)

    with open(filepath, 'a') as f:  
        f.write(f"Results for file: {inputfile}\n")
        f.write(f"GC content: {gc_content}\n")
        f.write(f"Nucleotide frequency: {nucleotides}\n")
        f.write(f"DNA Sequence Length: {length}\n")
        f.write(f"Reverse Complement: {reverse}\n")
        f.write(f"RNA sequence: {rna}\n\n")
    print(f"Data written to file {filepath} for {inputfile}")

def processfile(inputfiles, outputfile):
    sequences = [] 
    labels = []  
    with open(outputfile, 'w') as f:
        f.write("DNA Sequence Analysis Results\n\n")
    for inputfile in inputfiles:
        if not os.path.exists(inputfile):
            raise FileNotFoundError(f"The file {inputfile} does not exist.")
        print(f"Processing file: {inputfile}")
        sequence = readfastafile(inputfile)  
        sequences.append(sequence) 
        labels.append(os.path.basename(inputfile)) 
        data = [
            sequence,
            calculateGCvalues(sequence),
            getnucleotides(sequence),
            calculatelength(sequence),
            reversecomplement(sequence),
            DNAtoRNA(sequence),
        ]
        writeoutput(outputfile, data, inputfile)  

    Heatmap(sequences, labels)
    plotGCcontent(sequences, labels) 
    ScatterplotGC_vs_lenght(sequences, labels)  
    plotnucleotidefrequency(sequences, labels)


