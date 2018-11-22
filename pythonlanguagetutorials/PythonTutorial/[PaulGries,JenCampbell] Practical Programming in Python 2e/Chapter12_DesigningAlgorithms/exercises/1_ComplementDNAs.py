

class DNASequence:
    """A DNA sequence made up of letters A T, G, C."""
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def complement(self):
        # A -> T, C -> G, G -> C
        oppositeDict = {"A":"T", "T":"A", "G":"C", "C":"G"}
        seq = ""

        for letter in self.sequence:
            seq += oppositeDict[letter]
        return seq


if __name__ == "__main__":
    dna = DNASequence("AATTGCCGT")
    print(dna)
    assert dna.complement() == "TTAACGGCA"
    assert DNASequence(dna.complement()).complement() == dna.sequence