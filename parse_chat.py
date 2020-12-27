def search(t, phrase):
	for x in range(len(t)):
		if(phrase in t[x]):
			print(x)

f = open("chat.txt", "r")
s = []
for x in range(69):
	s.append(set())
while True:
	li = f.readline()
	if(not li):
		break
	t = tuple(map(str, li.split(", ")[1:-1]))
	print(t)

print(s[0])
print(len(s[0]))
f.close()
