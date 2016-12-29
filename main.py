#!/usr/bin/env python2

from rivescript import RiveScript

rs = RiveScript()
rs.load_directory("./brain")
rs.sort_replies()


while True:
    msg = raw_input("You> ")
    if msg == '/quit':
        quit()
    reply = rs.reply("localuser", msg)
    print "Bot>", reply
