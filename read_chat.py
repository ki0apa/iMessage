import sqlite3
from sqlite3 import OperationalError
from shutil import copyfile

def run(query):
	cur.execute(query) 
	ar = []
	for name in cur.fetchall():
	    ar.append(name)
	return ar

def getChatID(message):
	ar = run(" SELECT * FROM message WHERE text='" + message + "'")
	message_id =ar[0][0]
	return run(" SELECT chat_id, message_id FROM chat_message_join where message_id=" + str(message_id))[0][0]


def test(query):
	cur.execute(query) 
	d = dict()
	for name in cur.fetchall():
		if(name[0] in d):
			d[name[0]] += 1
		else:
			d[name[0]] = 1
	print(d)


conn = sqlite3.connect('chat.db')
cur = conn.cursor()

#put a unique message from the group chat
unique = "does anyone have a dress shirt that I can borrow for tonight"

f = open("sql.txt", "r")
f1 = open("chat.txt", "w")
s = set()
for x in run(f.read().replace("{CHAT_ID}", str(getChatID(unique)))):
	f1.write(str(x) + "\n\n")
f.close()
f1.close()

f = open("sql1.txt", "r")
f1 = open("images.txt", "w")
s = set()
c = 0
for x in run(f.read().replace("{CHAT_ID}", str(getChatID(unique)))):
	f1.write(str(x) + "\n\n")
	rev = x[0][::-1]
	name = rev[:rev.find("/")][::-1]
	copyfile(x[0].replace("~/Library/Messages/", ""), "images/" + name)
f.close()
f1.close()
