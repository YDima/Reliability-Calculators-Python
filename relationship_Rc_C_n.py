import math

print("Enter what you want to calculate: or Rc, or C, or n:")
info = input()


def enter(a, b):
    a = input(f"Enter {a}")
    b = input(f"Enter {b}")
    return a, b


def enterIfValueNegOrMore1(v, msg):
    while v < 0.0 or v > 1.0:
        print("Value must be from 0.0 to 1.0")
        v = float(input(f"Enter {msg} :"))
    return v


if info == "Rc":
    C = "Confidence (C): "
    n = "Sample size (n): "
    C, n = enter(C, n)
    # print("Confidence (C): ", C)
    # print("Sample size (n): ", n)
    C = float(C)
    if C < 0.0 or C > 1.0:
        C = enterIfValueNegOrMore1(C, "Confidence (C)")
    n = abs(int(n))
    Rc = math.pow((1 - C), 1 / n)
    print("Reliability at confidence (Rc): ", round(Rc, 2), "%")

if info == "C":
    Rc = "Reliability at confidence (Rc): "
    n = "Sample size (n): "
    Rc, n = enter(Rc, n)
    # print("Reliability at confidence (Rc): ", Rc)
    # print("Sample size (n): ", n)
    Rc = float(Rc)
    if Rc < 0.0 or Rc > 1.0:
        Rc = enterIfValueNegOrMore1(Rc, "Reliability at confidence (Rc)")
    n = abs(int(n))
    # print(Rc**(n+1))
    # print(math.pow(Rc,n+1))
    C = 1 - math.pow(Rc, n + 1)
    print("Confidence (C): ", round(C, 2), "%")

if info == "n":
    C = "Confidence (C): "
    Rc = "Reliability at confidence (Rc): "
    C, Rc = enter(C, Rc)
    # print("Confidence (C): ", C)
    # print("Reliability at confidence (Rc): ", Rc)
    C = float(C)
    if C < 0.0 or C > 1.0:
        C = enterIfValueNegOrMore1(C, "Confidence (C)")
    Rc = float(Rc)
    if Rc < 0.0 or Rc > 1.0:
        Rc = enterIfValueNegOrMore1(Rc, "Reliability at confidence (Rc)")
    n = math.log10(1 - C) / math.log10(Rc) - 1
    print("Sample size (n): ", math.floor(n))
