def setContext(acctDict, customerDict):
    userContext = None
    userAuthenticated = False


    userName = input("Please enter a user name: ").strip()
    password = input("Please enter a password: ").strip()

    try:
       userAuthenticated = authenticateUser(userName, password, acctDict)
    except RuntimeError as e:
        print(e)

    if userAuthenticated:
        cust_id = acctDict[userName].getCustId()
        userContext = customerDict[cust_id]

    return userContext



def authenticateUser(userName, password, acctDict):
    authenticated = False
    if userName in acctDict:
        if acctDict[userName].getPassword() == password:
            authenticated = True
        else:
            raise RuntimeError("Invalid UserName/Password")
    else:
        raise RuntimeError("Invalid UserName/Password")
    return authenticated