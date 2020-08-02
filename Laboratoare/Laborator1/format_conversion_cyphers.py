import formats

C1 = "000100010001000000001100000000110001011100000111000010100000100100011101000001010001100100000101"
C2 = "02030F07100A061C060B1909"
K = "abcdefghijkl"

def xor_bin(cyphertext_bin, key_bin):
	return formats.bin2str(formats.bitxor(cyphertext_bin, key_bin)).decode("ASCII")

def decrypt_bin(cyphertext_bin, key):
	key_bin = formats.str2bin(key)
	return xor_bin(cyphertext_bin, key_bin)

def decrypt_hex(cyphertext_hex, key):
	key_bin = formats.str2bin(key)
	cyphertext_bin = formats.hex2bin(cyphertext_hex)
	return xor_bin(cyphertext_bin, key_bin)

if __name__ == "__main__":
	print("The decoded message from cyphertext C1 = " + decrypt_bin(C1, K))
	print("The decoded message from cyphertext C2 = " + decrypt_hex(C2, K))