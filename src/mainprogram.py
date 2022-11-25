from argparse import ArgumentParser
from processFile import create_token
from bacagrammar import read_a_grammar
from converterofGrammar import CFGtoCNF
from parserOfGrammar import CYK_parse

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")
    args = arg_parser.parse_args()
    if CYK_parse(CFGtoCNF(read_a_grammar("grammar.txt")), create_token(args.nama_file)):
        print("Accepted")
    else:
        print("Syntax Error")