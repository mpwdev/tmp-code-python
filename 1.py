
# Write a function called get_vat() with 2 parameters, price and vat percentage
# It calculates and returns the VAT (value-added tax).
# YOUR CODE STARTS HERE

def get_vat(price, vat_percentage):
	vat = price * (vat_percentage / 100)
	return vat
	


# Capture the returned value in a new variable called vat.
vat = get_vat(100, 20)
print(f' vat is: {vat} %')