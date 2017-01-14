#!/usr/bin/env python2

# pip2 install unicodecsv


from rivescript import RiveScript

rs = RiveScript('utf8:true')
rs.load_directory("./brain")
rs.sort_replies()

while True:
	msg = raw_input("You> ")
	if msg == '/quit':
		quit()
	reply = rs.reply("localuser", msg)
	print "Bot>", reply
