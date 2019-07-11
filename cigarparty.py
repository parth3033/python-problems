def cigar_party(n,w):
		if w ==True:
			if n>40:
				return True
			else:
				return False
		elif w ==False:
			if n<60 and n>40:
				return True
			else:	
				return False
	print(cigar_party(30,False))
	print(cigar_party(50,False))
	print(cigar_party(70,True))


