teste = "este e o teste %s"
string = "de uma string"

print teste %string

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' 
print "And everywhere that Mary went." 
print "." * 10 # what'd that do? 
end1 = "C" 
end2 = "h" 
end3 = "e" 
end4 = "e" 
end5 = "s" 
end6 = "e" 
end7 = "B" 
end8 = "u" 
end9 = "r" 
end10 = "g" 
end11 = "e" 
end12 = "r" 

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6 
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r" 
print formatter % (1, 2, 3, 4) 
print formatter % ("one", "two", "three", "four") 
print formatter % (True, False, False, True) 
print formatter % (formatter, formatter, formatter, formatter) 
print formatter % ( "I had this thing.",
    "That you could type up right.",
	   "But it didn't sing.", 
	   "So I said goodnight." )

print #comentario intrometido

print """outro 
comentario 
intrometido
"""

while True:
for i in ["/","-","|","\\","|"]:
print "%s\r" %i