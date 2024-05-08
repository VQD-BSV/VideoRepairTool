import os, binascii

with open("REF.AVI", "rb") as r:
	data = r.read()

with open("Corrupted.AVI", "rb") as r:
	data_2 = r.read()


header = data.find(binascii.unhexlify('FFFFFFFFFF'))
data_fix = data_2.find(binascii.unhexlify('FFFFFFFFFF'))

with open("HEX", "wb") as w:
	w.write(data[:header - 16])

with open("HEX", "ab") as a:
	a.write(data_2[data_fix - 16:])
