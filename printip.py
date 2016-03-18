with open('subnet.txt', 'r') as f:
    contents = f.read()

contents = contents.split('\n')

ips = []
for ip in contents:
	for i in range(255):
		full_ip = ip.strip() + str(i) + '\n'
    		ips.append(full_ip)
	

with open('ips.txt', 'w') as f:
    f.writelines(ips)



