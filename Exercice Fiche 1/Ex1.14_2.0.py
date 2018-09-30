# -*- coding: utf-8 -*
string = input("Leet speak : ").upper()
leetstring = string

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
leetspeak = ["4","8","<","|)","3","|=","[,","|=|","1","_|","|<","|_","/x\\","|\\|","0","|O","(,)","R","5","7","|_|","\\/","\\X/","%","¥","7_"]

for i in range(0,26):
	leetstring=leetstring.remove(alphabet[i],leetspeak[i])