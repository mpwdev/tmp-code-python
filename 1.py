
import subprocess
command = 'ping -n 1 8.8.8.8'
output = subprocess.check_output(command.split())
print(output.decode())