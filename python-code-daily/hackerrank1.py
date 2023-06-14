stri = "AweSome Is CodinG"
stril = list(stri)
for i in range(len(stril)):
    if stril[i].islower():
        stril[i] = stril[i].upper()
    elif stril[i].isupper():
        stril[i] = stril[i].lower()
stri = "".join(stril).split(" ")
print(" ".join(stri[::-1]))