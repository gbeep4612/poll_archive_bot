import time

def getUrl(url,fn):
	cmd = "curl --silent "+url+" > "+fn
	os.system(cmd)
	return fn

last_message_sent = None
while True:
	url = "https://www.archives.gov/electoral-college/2020"
	fn = "temparchive"
	getUrl(url,fn)
	with open(fn,"r") as fp:
		lines = fp.readlines()
		dashcount = 0
		for line in lines:
			for char in line:
				if char == '-':
					dashcount = dashcount + 1
		#print("dashcount: "+str(dashcount))
		if dashcount != 895:
			print("Electoral College page at the national archives has changed.")
			#last_message_sent = piBot.SendSMSToAdmin("Archive page changed.",last_message_sent)
	time.sleep(60)