import random

prime = 26994308385016394749558484505346578147056894665639
g=2


def genprivate(filename):
	x=str(random.randint(1000,10000))
	with open(filename,'w') as outfile:
		outfile.write(x)


def genpublic(privatefilename,publicfilename):
	with open(privatefilename,'r') as infile:
		private = infile.read()
	private=int(private)
	public = (g**private)%prime
	public = str(public)
	with open(publicfilename,'w') as outfile:
		outfile.write(public)



def gensecret(privatefile,publicfile):
	with open(privatefile,'r') as infile:
		pri = int(infile.read())
	with open(publicfile,'r') as infile:
		pub = int(infile.read())
	secret = (pub**pri)%prime
	return secret