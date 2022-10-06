from audioop import mul


def multiple(a, b, n):
    output = []
    for i in range(1, n+1):
        if(a*i <= n):
            output.append(a*i)
        if(b*i <= n):
            output.append(b*i)
    return sorted(list(set(output)))

print(multiple(7,3,30))