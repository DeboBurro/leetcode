# User db scheme
#      { 
#           USER_NAME(str) : { 
#               'LOG_IN' : (bool),
#               'HASH_PWD' : (str) 
#           }
#      }
USER_DB = dict()

# Better using enum
UNSUCC_REGISTER_MSG = {'UNAME_EXISTS' : 'Username already exists'}
SUCC_REGISTER_MSG = 'Registered Successfully'
UNSUCC_LOGIN_MSG = 'Login Unsuccessfully'
SUCC_LOGIN_MSG = 'Logged In Successfully'
UNSUCC_LOGOUT_MSG = 'Logout unsuccessfully'
SUCC_LOGOUT_MSG = 'Logged Out Successfully'



def register(u_name, pwd):
    if u_name in USER_DB:
        return UNSUCC_REGISTER_MSG['UNAME_EXISTS']
    USER_DB[u_name] = { 'LOG_IN': False, 
                        'HASH_PWD' : str(hash(pwd))
                        }
    return SUCC_REGISTER_MSG

def login(u_name, pwd):
    if u_name not in USER_DB:
        return UNSUCC_LOGIN_MSG
    if str(hash(pwd)) != USER_DB[u_name]['HASH_PWD']:
        return UNSUCC_LOGIN_MSG
    if USER_DB[u_name]['LOG_IN']:
        return UNSUCC_LOGIN_MSG
    USER_DB[u_name]['LOG_IN'] = True
    return SUCC_LOGIN_MSG

def logout(u_name):
    if not USER_DB[u_name]['LOG_IN']:
        return UNSUCC_LOGOUT_MSG
    USER_DB[u_name]['LOG_IN'] = False
    return SUCC_LOGOUT_MSG



def ImplementAPI(requests):

