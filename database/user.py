import connetion

def showAllUsers():
    connetion.databaseCursor.execute('select * from user;')
    users = connetion.databaseCursor.fetchall()
    return users

if __name__ == '__main__':
    print(showAllUsers())   