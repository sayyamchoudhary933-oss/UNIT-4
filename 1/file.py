def write_file(filename,content):
    with open(filename,"w")as file:
        file.write(content)
        print("the content is written")

def read_file(filename):
    try:
        with open(filename,"r")as file:
            content=file.read()
            print("content on file",content)
    except FileNotFoundError:
        print("file not found")

def append_file(filename,content):
    with open(filename,"a")as file:
        file.write(content)
        print("the appended line is ", content)

write_file("sample.txt","this is the first line\n")
read_file("sample.txt")
append_file("sample.txt","this is the appended line")
read_file("sample.txt")
