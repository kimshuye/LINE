from line import LineClient, LineGroup, LineContact,User

try:
    client = LineClient(User.data[0]['email'], User.data[0]['password'])
    #client = LineClient(authToken="AUTHTOKEN")
    
except:
    print "Login Failed"

#authToken = client.authToken
#print (authToken)

while True:
    op_list = []

    for op in client.longPoll():
        op_list.append(op)

    for op in op_list:
        sender   = op[0]
        receiver = op[1]
        message  = op[2]
        
        msg = message.text
        receiver.sendMessage("[%s] %s" % (sender.name, msg))

        try:
            msg = message.text
            receiver.sendMessage("[%s] %s" % (sender.name, msg))
        except  Exception, e:
            print str(e)
        else:
            break
        finally:
            break

print "Line End"
