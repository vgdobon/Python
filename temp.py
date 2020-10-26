
"""
result = ""
orig = ""
for c in text:
    if c >= " ":
        # Quitar \n, etc.
        orig = orig + c
for i in range(len(orig)):
    if i > 2:
        if ( orig[i-3].isupper() and orig[i-2].isupper() and orig[i-1].isupper()
            and orig[i+1].isupper() and orig[i+2].isupper() and orig[i+3].isupper()
            and orig[i].islower() and orig[i] == "c"):
            print(orig[i-3:i+4])