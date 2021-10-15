"""
#
# @File         : Question02.py
# @Created      : 2021-10-11 11:17
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : python script to encrypt a password. Use the timeit function to time it takes to encrypt the data.
#
"""

if __name__ == "__main__":
    '''
       Main method of application :

       Parameters:
        none
       Returns:
        none
    '''

    import timeit
    from cryptography.fernet import Fernet


    def passwordEncrypt(passwd):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(passwd.encode())
        print(encMessage)
        return


    password = input("Enter your password : ")
    print(passwordEncrypt(password))
    print(timeit.timeit("passwordEncrypt(passwd)",
                        setup="from __main__ import passwordEncrypt; message = 'Hello'",
                        number=1))
