# this is program to break document into chunks 


def chunkify(string):
	str_arr = string.split(":")
	document = []
	buff = ""

	for s in str_arr[ : -1]:
		if len(buff) > 3:
			document.append(buff)
			buff = ""

		if not buff:
			if len(s) > 3:
				document.append(s)
			else:
				buff += s

		elif len(s) + len(buff) <= 3:
			buff += s
			document.append(buff)
			buff = ""

		else:
			document.append(buff)
			buff = ""
			buff += s

	return document

print(chunkify("a:abe:aedsfsdf:asdf:e:fs:sdff:s:ab:"))



