import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors): #define the function main, which has three parameters
    line = language_file.readline() #langugage_file is the actual parameter, encoding and errors are two formal parameters

    if line: #if-statement is used to determine whether its true or not. if true, execute the following lines, if false it will not execute to prevent infinite loops
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) #is to call main again and return back to the beginning and call the file again

# the function of the function below is to encode each line in languages.txt
def print_line(line, encoding, errors): #this is to define the print_line which has three parameters
    next_lang = line.strip() #strip()Remove the \n at the end of each line
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string) #to print <===> where the left side is the byte string and the right is the string


languages = open("languages.txt", encoding="utf-8") #this is to open languages.txt in utf-8 encoding

main(languages, input_encoding, error)
