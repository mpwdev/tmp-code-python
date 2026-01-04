
import subprocess

with open('hosts.txt') as f:
	ips = f.read().splitlines()
	for ip in ips:
		try:
			command = f'ping -n 1 {ip}'
			output = subprocess.check_output(command.split())
			print(output.decode())
		except Exception as e:
			print(f'Error pinging {ip}: {e}')
		print('=' * 20)

print(ips)