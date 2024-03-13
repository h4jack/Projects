from sys import argv

def print_help():
    print("""Help:
    This is a pdf to docx converter made using python.
    This takes pdf file_name or pdf file_path as argument/input and converts to docx file.

    *Note: Make sure your entered file is valid/exists.
    """)
    print_usage()

def print_usage():
    print(f"""
Usage:
    py {argv[0]} file_1.pdf
    py {argv[0]} file_1.pdf file_2.pdf file_n.pdf 
OR:
    python {argv[0]} file_1.pdf
    python {argv[0]} file_1.pdf file_2.pdf file_n.pdf
""")

def print_error(message):
    print(message)
    print()
    print("You can try the help option to get full help")
    print(f"$> {argv[0]} help")