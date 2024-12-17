import argparse
from pathlib import Path
from .operations import processfile 

def getfastafiles(input_path):
    input_path = Path(input_path)
    if input_path.is_dir():
        fasta_files = list(input_path.glob('*.fasta'))
        if not fasta_files:
            raise FileNotFoundError(f'No FASTA files found in {input_path}')
        return [str(file) for file in fasta_files]
    elif input_path.is_file() and input_path.suffix == '.fasta':
        return [str(input_path)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNA analysis organizer')

    parser.add_argument('--input',
                        dest='input_files',
                        required=True,
                        help='paths to input FASTA files')  
    parser.add_argument('--output',
                        dest='output_file',
                        required=True,
                        help='path to output file')

    args = parser.parse_args()
    input_files = getfastafiles(args.input_files)
    processfile(input_files, args.output_file)



