#get email address
email = input("Enter email address: ").strip()
#slice out user name
user_name = email[:email.index("@")]
#slice Domain name
domain_name = email[email.index("@")+1:]
#format message
message = "User Name : {} \nDomain Name : {}".format(user_name,domain_name)
#display output message
print(message)
