#!/usr/bin/python
import urllib
import pycurl
import json
import StringIO

STREAM_URL = "http://stream.twitter.com/1/statuses/filter.json"

class Client:
	def __init__(self):
		self.buffer = ""
		self.conn = pycurl.Curl()

	def connect(self):
		self.conn.setopt(pycurl.URL, STREAM_URL)
		self.conn.setopt(pycurl.USERPWD, "%s:%s" % (self.username, self.password))
		data = urllib.urlencode([('track', self.username)])
		self.conn.setopt(pycurl.POSTFIELDS, data)
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)
		self.conn.perform()

	def on_receive(self, data):
		self.buffer += data
		if data.endswith("\r\n") and self.buffer.strip():
			content = json.loads(self.buffer)
			self.buffer = ""
			#do something with the result
			#most usefull variables
			#username of sender: content['user']['screen_name']
			#text of mention:    content['text']

client = Client()
client.username = '' #username
client.password = '' #password
client.connect()
