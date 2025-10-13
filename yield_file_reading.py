#using yield function , reading a file
def read_large_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()
for line in read_large_file("hospital_logsl.txt"):
    print(line)