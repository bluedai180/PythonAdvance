a = "a.sh"
b = "b.py"
c = "c.cpp"

l = [a, b, c]
print([x for x in l if x.endswith((".sh", ".py"))])