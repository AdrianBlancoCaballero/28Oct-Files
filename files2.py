f = open("archivo.data", "r")
line = f.readline()
while(line != ""):
    print("\n", line)
    line = f.readline()
f.close()

f = open("archivo.data", "r")
for line in (f):
    print("\n", line)
f.close()

f = open("archivo.data", "r")
lines = list(f)
print("\n", lines)
f.close()