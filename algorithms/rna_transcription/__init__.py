def to_rna(dnastrand):
    d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(d[x] for x in dnastrand)
