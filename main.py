print('Create Account')
username = input('Enter username: ')
password = input('Enter password: ')

print(f'User {username} created successfully!')
print('Login now!')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username2 == username and password2 == password:
    print('User logged in successfully')
else:
    print('Invalid Credentials')

