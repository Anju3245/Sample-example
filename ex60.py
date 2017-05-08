from sys import argv
script,from_file,to_file = argv

def rewind(f):
    f.seek(5)
#print(f"Copying from {from_file} {to_file}")
in_file=open(from_file)
indata=in_file.read()
#name=input()
out_file=open(to_file,'w')
out_file.write(indata+#+ name)
