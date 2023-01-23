def inversions(s):
    s = s.split(" ")
    s[0], s[1] = s[1], s[0]

    return " ".join(s)

print(inversions("BLIP BLOOP"))