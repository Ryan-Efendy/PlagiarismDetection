from argparse import ArgumentParser
from plagiarism_detector import PlagiarismDetector


def main():
    parser = ArgumentParser(
        description='Command Line Tool for Plagiarism Detection')

    parser.add_argument('-f', '--files', required=True,
                        nargs=2, help='Two files to compare for plagiarism', )
    parser.add_argument('-s', '--synonyms', required=True,
                        help='Synonyms file', )
    parser.add_argument('-t', '--tuple_size', type=int,
                        help='Size of the tuple', )

    args = parser.parse_args()

    file1, file2 = args.files
    synonyms = args.synonyms
    tuple_size = args.tuple_size if args.tuple_size else PlagiarismDetector.DEFAULT_TUPLE_SIZE

    print("File Path 1: {}\nFile Path 2: {}\nSynonyms Path: {}\nTuple Size: {}\n".format(file1, file2,
                                                                                         synonyms,
                                                                                         tuple_size))
    print("Percentage Plagiarized: {}".format(PlagiarismDetector(file1, file2, synonyms,
                                                                 tuple_size).get_plagiarized_percentage()))


if __name__ == '__main__':
    main()
