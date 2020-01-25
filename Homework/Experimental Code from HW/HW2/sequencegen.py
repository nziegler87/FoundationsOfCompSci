a = int(input("a:"))
d = int(input("d:"))
n = int(input("n:"))

output_string = []

for x in range (n):
    if (x + 1) == 1:
        output_string.append("a" + str((x + 1)) + ": " + str(a))
    else:
        value = a + (d * x)
        output_string.append("a" + str(x + 1) + ": " + str(value))

print("\nOutput:")
print("\n".join(output_string))
