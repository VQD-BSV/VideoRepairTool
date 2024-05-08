def V_AVI():
	print("""
	# os, binascii
	# data = REF & data_2 = Corrupted
	
	header, data_fix = data.find(binascii.unhexlify('FFFFFFFFFF')), data_2.find(binascii.unhexlify('FFFFFFFFFF'))
	File = data[:header - 16] + data_2[data_fix - 16:] """)
def V_MP4_MOV():
	
