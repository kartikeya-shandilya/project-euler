
import sys
import random
from goto import goto, comefrom, label

def function(string,n):
	if string=="miiii":
		print "done"
		sys.exit()
	else:
		label .myLabel
		i=random.randint(0,3)
		if i==0:
			k=0
			for j in xrange(len(string)-2):
				print "0",string[j:j+2]
				if string[j:j+2]=="iii":
					k=1
					print string[:j-1]+"u"+string[j+3:]
					function(string[:j-1]+"u"+string[j+3:],n+1)
					goto .myLabel
#			if k==0:
#				return
		elif i==1:
			k=0
			for j in xrange(len(string)-1):
				print "1",string[j:j+2]
                       	        if string[j:j+1]=="uu":
					k=1
					print string[:j-1]+string[j+2:]
	                                function(string[:j-1]+string[j+2:],n+1)
					goto .myLabel
#			if k==0:
#				return
		elif i==2:
			print "2",string[len(string)-1:]
               	        if string[len(string)-1:]=="i":
				print string+"u"
                               	function(string+"u",n+1)
				goto .myLabel
#			else:
#				return
		else:
			print "m"+string[1:]*2
			function("m"+string[1:]*2,n+1)
			goto .myLabel
#	return


function("mi",0)

