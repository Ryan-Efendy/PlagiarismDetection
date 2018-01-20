## Plagiarism Checker

### Summary

**This program checks the similarity of two files, accounting for synomyms.**

### Description

This is a command-line program that performs plagiarism detection using a N-tuple comparison algorithm allowing for synonyms in the text.

It takes in 3 required arguments, and one optional.

File name for a list of synonyms
Input file 1
Input file 2
(optional) the number N, the tuple size. If not supplied, the default is N=3.
The synonym file has lines each containing one group of synonyms. For example a line saying "run sprint jog" means these words should be treated as equal. The input files should be declared plagiarized based on the number of N-tuples in file1 that appear in file2, where the tuples are compared by accounting for synonyms as described above. For example, the text ";go for a run" has two 3-tuples, ["go for a", "for a run"] both of which appear in the text "go for a jog". The output of the program should be the percent of tuples in file1 which appear in file2. So for the above example, the output would be one line saying "100%". In another example, for texts "go for a run" and "went for a jog" and N=3 we would output "50%" because only one 3-tuple in the first text appears in the second one.

### Requirements

Python3

### How to run

```
$ python main.py -f tests/test2/file1.txt tests/test2/file2.txt -s tests/test2/syns.txt -t 3

or

$ python main.py --files tests/test2/file1.txt tests/test2/file2.txt --synonyms tests/test2/syns.txt --tuple_size 3

File Path 1: tests/test2/file1.txt
File Path 2: tests/test2/file2.txt
Synonyms Path: tests/test2/syns.txt
Tuple Size: 3

Percentage Plagiarized: 50.0
```

```
$ python main.py --files tests/test1/file1.txt tests/test1/file2.txt --synonyms tests/test1/syns.txt --tuple_size 3

File Path 1: tests/test1/file1.txt
File Path 2: tests/test1/file2.txt
Synonyms Path: tests/test1/syns.txt
Tuple Size: 3

Percentage Plagiarized: 100.0
```

```
$ python main.py --files tests/test1/file1.txt  --synonyms tests/test1/syns.txt

usage: run.py [-h] -f FILES FILES -s SYNONYMS [-t TUPLE_SIZE]
main.py: error: argument -f/--files: expected 2 argument(s)
```

### Algorithms & Data Structures

1. Parses the synonyms file and create a dictionary/HashMap where the key is the synonyms and the value is the **first** synonym.

Example: "run sprint jog"

```
{
    "sprint": "run",
    "run": "run",
    "jog": "run"
}
```

2. Converts a file to a list of overlapping tuples.
   1. To save computation time, it checks if any of the words in the files are in the synonyms HashMap/dictionary if they are replace it with the value.
   2. Create a list of N sized tuples of both the source and target files

```
Example: "go for a jog"

is replaced with: "go for a run"
```

```
Example: "went for a sprint"

[("went","for","a"), ("for","a","run")]
```

3. Check if any of the tuple in the target is in the source if so increment the plagiarized count

### Algorithmic complexity & runtime

time: O(n^2)

### Assumptions

* The Synonyms text file must be correctly formatted. It won't throw an error but it might not give the right substitutions if is not in the line by line format as stated
