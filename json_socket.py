import socket
import json
import time
import pickle

class server():
	def __init__(self, ip ='', port = 12345):
		self.ip = ip
		self.port = port
		self.data = { "name":"John", "age":30, "city":"New York"}
		self.received_data = ''
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def tcp_bind(self):
		try:
			self.sock.bind((self.ip, self.port))
			self.sock.listen()
			self.conn, self.addr = self.sock.accept()
		except:
			try:
				self.conn.close()
			except:
				pass
			self.sock.close()
				
	def send_data(self):
		try:
			self.conn.sendall(pickle.dumps(self.data))
		except Exception as e:
			print("Data cannot be sent with error: {}".format(e))
			
	def receive_data(self, data_length=1024):
		try:
			self.received_data = json.load(pickle.loads(self.conn.recv(data_length)))
			print("Data received:",self.received_data)
		except Exception as e:
			print("Data cannot be received with error: {}".format(e))
		return self.received_data
		
	def tcp_close(self):
		self.sock.close()
			
class client():
	def __init__(self, ip ='', port = 12345, data = {'name': 'John', 'age': 30, 'city': 'New York'}
):
		self.ip = ip
		self.port = port
		self.data = data
		self.received_data = ''
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	
	def tcp_connect(self):
		try:
			self.sock.connect((self.ip, self.port))
		except Exception as e:
			print("Unable to connect with error: {}".format(e))
			self.sock.close()
			
	def send_data(self):
		try:
			self.sock.sendall(pickle.dumps(self.data))
		except Exception as e:
			print("Data cannot be sent with error: {}".format(e))
			
	def receive_data(self, data_length=1024):
		try:
			self.received_data = json.load(pickle.loads(self.sock.recv(data_length)))
			print("Data received:",self.received_data)
		except Exception as e:
			print("Data cannot be received with error: {}".format(e))
		return self.received_data
			
	def tcp_close(self):
		self.sock.close()
