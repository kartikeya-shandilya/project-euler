
import string
letters = string.ascii_uppercase

def maximax(n):
	solved = letters[:n]
	solved = solved[:n-2]+solved[n-2:][::-1]
	result = [solved[:n-3]+solved[n-3:][::-1]]
	cnt = n-3
	for i in xrange(n-2):
		new_result = []
		for strng in result:
			for j in xrange(cnt+1, n-1):
				new_result.append(strng[:j] + strng[j:][::-1])
		result = []
		for strng in new_result:
			result.append(strng[:cnt-1]+strng[cnt-1:][::-1])
		cnt -= 1
	return result

print sorted(maximax(11))[2010]

