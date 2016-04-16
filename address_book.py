def adress():

    while True:
        user = raw_input("please enter the name: ")
        flag = verify_add(user)
        if flag:
            if user == "exit":
                break
            address = raw_input("please enter the address: ")

            add_address(user,address)
        else:
            print "Invalid"

    ask = raw_input("enter the name to find the address:")
    result = get_detail(ask)
    print result

def verify_add(user):
    try:
        fh = open("address.txt","r")
        for line in fh.readlines():
            if user in line:
                fh.close()
                return False
        fh.close()
        return True
    except IOError:
        fh = open("address.txt","w")
        fh.close()
        return True


def add_address(user,address):
    fh = open("address.txt","a+")
    data = "%s %s\n" %(user,address)
    fh.write(data)
    fh.close()


def get_detail(user):
    fh = open("address.txt","r")
    for line in fh.readlines():
        if user in line:
            return line
    return "user not in address book"

adress()

