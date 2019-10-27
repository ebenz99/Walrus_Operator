import math

def main():
	walrus = False
	if walrus:=True:
		print("Hello " + "".join([chr(ord(letter)+3+(idx*4//3)) if math.sin(1.1*idx)-.1 < 0 else chr(ord(letter)-3) for idx,letter in enumerate(str(walrus))])+"d")

if __name__ == "__main__":
	main()
