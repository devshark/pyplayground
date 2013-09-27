#!/bin/python

import string

orig = string.ascii_lowercase
repl = string.ascii_lowercase[2:26]+"ab"
encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".lower()
table = string.maketrans(orig,repl)
print encrypted.translate(table)

print "map".translate(table)


##
##decrypted = ""
##
##
##
##for index in range(0, len(encrypted)):
##    for letter in range(0,len(alphabet)):
##        if not encrypted[index] in alphabet:
##            decrypted += encrypted[index]
##            break
##        elif encrypted[index] == alphabet[letter]:
##            decrypted += alphabet[letter+2]
##            break
##
##print decrypted
