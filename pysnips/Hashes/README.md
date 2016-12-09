# HASHES

## RNA to Protein sequence translation

The central dogma of molecular biology is that DNA is transcribed into RNA, which is then tranlsated into protein. RNA, like DNA, is a long strand of nucleic acids held together by a sugar backbone (ribose in this case). Each segment of three bases is called a codon. Molecular machines called ribosomes translate the RNA codons into amino acid chains, called polypeptides which are then folded into a protein.

Protein sequences are easily visualized in much the same way that DNA and RNA are, as large strings of letters. An important thing to note is that the 'Stop' codons do not encode for a specific amino acid. Their only function is to stop translation of the protein, as such they are not incorporated into the polypeptide chain. 'Stop' codons should not be in the final protein sequence. To save a you a lot of unnecessary (and boring) typing the keys and values for your amino acid dictionary are provided.

Given a string of RNA, create a funciton which translates the RNA into its protein sequence. Note: the test cases will always produce a valid string.
```python
protein('UGCGAUGAAUGGGCUCGCUCC') returns 'CDEWARS'
```

Included as test cases is a real world example! The last example test case encodes for a protein called green fluorescent protein; once spliced into the genome of another organism, proteins like GFP allow biologists to visualize cellular processes!

Amino Acid Dictionary
```python
    # Phenylalanine
    'UUC':'F', 'UUU':'F',
    # Leucine
    'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L','CUA':'L','CUG':'L', 
    # Isoleucine
    'AUU':'I', 'AUC':'I', 'AUA':'I', 
    # Methionine
    'AUG':'M', 
    # Valine
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 
    # Serine
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 
    # Proline
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 
    # Threonine
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    # Alanine
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 
    # Tyrosine
    'UAU':'Y', 'UAC':'Y', 
    # Histidine
    'CAU':'H', 'CAC':'H',
    # Glutamine
    'CAA':'Q', 'CAG':'Q', 
    # Asparagine
    'AAU':'N', 'AAC':'N', 
    # Lysine
    'AAA':'K', 'AAG':'K',
    # Aspartic Acid
    'GAU':'D', 'GAC':'D', 
    # Glutamic Acid
    'GAA':'E', 'GAG':'E',
    # Cystine
    'UGU':'C', 'UGC':'C',
    # Tryptophan
    'UGG':'W', 
    # Arginine
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 
    # Glycine
    'GGU':'G',  'GGC':'G', 'GGA':'G', 'GGG':'G', 
    # Stop codon
    'UAA':'Stop', 'UGA':'Stop', 'UAG':'Stop'
```

> **FUNDAMENTALS**, **HASHES**, **DATA STRUCTURES**

## Square climber

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```
Hints:
> In case of input data being supplied to the question, it should be assumed to be a console input.

## Tuple Sorter

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

## Word Frequency

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

## Dictionary Square Keys

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
