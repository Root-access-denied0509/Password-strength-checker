import re
def check_password(password):
	errors = []
	if len(password) < 8:
		errors.append('At least 8 characters')
	if not re.search('[A-Z]', password):
		errors.append('At least one uppercase letter')
	if not re.search(r'[a-z]', password):
		errors.append('At least one lowercase letter')
	if not re.search(r'[0-9]', password):
		errors.append('At least one number')
	if not re.search(r'[!@#$%^&*]', password):
		errors.append('At least one special character')

	if errors:
		print('\n❌ Weak password. Your password needs:')
		for e in errors:
			print(f"     -{e}')")
	else:
		print('n✅ Strong password!')

password = input('Enter a password to check: ')
check_password(password)