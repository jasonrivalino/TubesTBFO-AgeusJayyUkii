def read_a_grammar(nama_file): # fungsi untuk membaca grammar dari file
    file = open(nama_file, "r")
    cfg = {}
    line = file.readline()
    while line != "":
        head,body = line.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))
        line = file.readline()
    file.close()
    return cfg

def cekTerminal(string): # fungsi untuk mengecek apakah string merupakan terminal
    list_of_terminal = [
        "EQUALS",
        "ISEQ",
        "KURUNG_DEPAN",
        "KURUNG_BELAKANG",
        "SEMICOLON",
        "COLON",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "POW",
        "LEQ",
        "L",
        "GEQ",
        "G",
        "NEQ",
        "AND",
        "OR",
        "NOT",
        "TRY",
        "CATCH",
        "FINALLY",
        "IF",
        "THEN",
        "ELSE",
        "WHILE",
        "FALSE",
        "TRUE",
        "NONE",
        "BREAK",
        "CONTINUE",
        "FUNCTION",
        "FOR",
        "RETURN",
        "WITH",
        "COMMA",
        "TITIK",
        "KURUNG_SIKU_DEPAN",
        "KURUNG_SIKU_BELAKANG",
        "KURUNG_KURAWAL_DEPAN",
        "KURUNG_KURAWAL_BELAKANG",
        "INT",
        "STRING",
        "SWITCH",
        "ID",
        "NEWLINE",
        "TYPE",
        "IDINT",
        "THROW"
        "CASE"
        "DEFAULT"
        "DELETE"
        "NULL"
    ]
    return string in list_of_terminal

def cekVariables(string):
    return not cekTerminal(string)