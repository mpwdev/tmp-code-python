import os
output = os.popen('arp -a').read()
print(output)
