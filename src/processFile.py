import sys
import re

token_exp = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "KURUNG_DEPAN"),
    (r'\)',                     "KURUNG_BELAKANG"),
    (r'\[',                     "KURUNG_SIKU_DEPAN"),
    (r'\]',                     "KURUNG_SIKU_BELAKANG"),
    (r'\{',                     "KURUNG_KURAWAL_DEPAN"),
    (r'\}',                     "KURUNG_KURAWAL_BELAKANG"),
    (r'\;',                     "SEMICOLON"), 
    (r'\:',                     "COLON"),
    (r'\*\*',                    "POW"),
    (r'\/\/',                    "FLOORDIV"),
    (r'/=',                      "DIVAS"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\=(?!\=)',               "EQUALS"),
    (r'\band\b',                "AND"),
    (r'\bor\b',                 "OR"),
    (r'\bnot\b',                "NOT"),
    (r'\bif\b',                 "IF"),
    (r'\btry\b',                "TRY"),
    (r'\bthen\b',               "THEN"),
    (r'\belse\b',               "ELSE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bFalse\b',              "FALSE"),
    (r'\bTrue\b',               "TRUE"),
    (r'\bNone\b',               "NONE"),
    (r'\bfunction\b',           "FUNCTION"),
    (r'\breturn\b',             "RETURN"),
    (r'\bwith\b',               "WITH"),
    (r'\bdict\b',               "TYPE"),
    (r'\bint\b',                "TYPE"),
    (r'\bstr\b',                "TYPE"),
    (r'\bfloat\b',              "TYPE"),
    (r'\bcomplex\b',            "TYPE"),
    (r'\blist\b',               "TYPE"),
    (r'\btuple\b',              "TYPE"),
    (r'\bset\b',                "TYPE"),
    (r'\,',                     "COMMA"),
    (r'\.',                     "DOT"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\bvar\b',                "VAR"),
    (r'\bconst\b',              "CONST"),
    (r'\blet\b',                "LET"),
    (r'\bcatch\b',              "CATCH"),
    (r'\switch\b',              "SWITCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bthrow\b',              "THROW"),
    (r'\default\b',             "DEFAULT"),
    (r'\delete\b',              "DELETE"),
    (r'\case\b',                "CASE"),
    (r'\null\b',                "NULL"),
]


newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, token_exp):
    pos = 0
    cur = 1
    line = 1
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("Illegal Character")
            print("Syntax Error")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)

if __name__ == "__main__":
    create_token('test.txt')