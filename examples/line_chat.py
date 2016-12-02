from line import LineClient, LineGroup, LineContact,User

USERNAME = User.data[0]['email']
PASSWORD = User.data[0]['password']
GROUPNAME = 'GroupTest'
MSG = 'send Message form bot!!!!'

#optional
COMPUTERNEME = 'kimshuye_bot'
TOKEN = ''

try:
  client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNEME)
  TOKEN = client.authToken
  print "TOKEN : %s\r\n" % TOKEN

  client_group = client.getGroupByName(GROUPNAME)
  recent_group_msg = client_group.getRecentMessages(count=10)
  print "RecentMessages : %s\r\n" % recent_group_msg

  client_group.sendMessage(MSG)

except:
    print "Login Failed"
