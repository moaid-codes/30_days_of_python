it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update({"Framework", "ASUS"})
print(it_companies)

it_companies.remove("Microsoft")
print(it_companies)

C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

AandB = A.union(B)
BandA = B.union(A)
print(AandB.union(BandA))

print(A.symmetric_difference(B))

del A, B

print(type(age))
print(len(age))
age = set(age)
print(len(age))


x = "I am a teacher and I love to inspire and teach people"
x = x.split()
x = set(x)
print(len(x))
