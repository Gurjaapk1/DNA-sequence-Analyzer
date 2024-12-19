import matplotlib.pyplot as plt
from .DNAsequenceanalyzer import calculatelength, reversecomplement, calculateGCvalues, getnucleotides, DNAtoRNA

def plotnucleotidefrequency(sequences, labels):    
    for i, sequence in enumerate(sequences):
        nucleotides = getnucleotides(sequence)  
        plt.figure(figsize=(6, 4))  
        plt.bar(nucleotides.keys(), nucleotides.values())  
        plt.xlabel("Nucleotides")
        plt.ylabel("Frequency")
        plt.title(f"Nucleotide Frequency - {labels[i]}")  
        plt.grid(axis='y', linestyle='--', alpha=0.7)   
        plt.show()

def plotGCcontent(sequences, labels):
    GC_values = [float(calculateGCvalues(seq).strip('%')) for seq in sequences]
    plt.figure(figsize=(8, 6))  
    bars = plt.bar(labels, GC_values)
    for bar, gc_value, label in zip(bars, GC_values, labels):
        plt.scatter(bar.get_x() + bar.get_width() / 2, gc_value, s=100, label=label, color=bar.get_facecolor())
        plt.annotate(f"{gc_value:.2f}%", 
                     (bar.get_x() + bar.get_width() / 2, gc_value), 
                     textcoords="offset points", xytext=(0, 5), ha='center')
    plt.xlabel("Sequences")
    plt.ylabel("GC Content (%)")
    plt.title("GC Content Across Sequences")
    plt.legend(title="Input Files")  
    plt.grid(axis='y', linestyle='--', alpha=0.7)  
    plt.show()


def ScatterplotGC_vs_lenght(sequences, labels):
    plt.figure(figsize=(10, 6))
    for i, seq in enumerate(sequences):
        GC_values = float(calculateGCvalues(seq).strip('%'))
        lengths = calculatelength(seq)
        plt.scatter(GC_values, lengths, label=labels[i])
        plt.annotate(labels[i], (GC_values, lengths), textcoords="offset points", xytext=(5, 5), ha='left')
    plt.xlabel("GC Content")
    plt.ylabel("Length")
    plt.title("GC content vs Length across multiple sequences")
    plt.legend(title="Input sequences")
    plt.grid(True)
    plt.show()

def Heatmap(sequences, labels):
    nucleotide_frequencies = []
    all_nucleotides = ['A', 'T', 'C', 'G']
    for sequence in sequences:
        nucleotides = getnucleotides(sequence)
        nucleotide_frequencies.append([nucleotides.get(base, 0) for base in all_nucleotides])
    plt.figure(figsize=(8, 6))
    plt.imshow(nucleotide_frequencies, cmap='hot', interpolation='nearest')
    plt.title("Heatmap of nucleotide frequency")
    plt.xlabel("Nucleotides")
    plt.ylabel("Sequences")
    plt.xticks(range(len(all_nucleotides)), all_nucleotides)
    plt.yticks(range(len(labels)), labels)
    plt.colorbar(label="Frequency")
    plt.show()







