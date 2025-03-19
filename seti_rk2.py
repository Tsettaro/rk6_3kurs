import ipaddress

def cidr_to_netmask(cidr):
    # Получаем количество бит маски сети из CIDR
    bits = cidr
    # Строим маску сети с использованием битов
    netmask = (1 << 32) - (1 << (32 - bits))
    # Преобразуем в формат 4 октетов
    netmask_parts = [
        (netmask >> 24) & 255,
        (netmask >> 16) & 255,
        (netmask >> 8) & 255,
        netmask & 255
    ]
    # Возвращаем маску в виде строки
    return '.'.join(map(str, netmask_parts))

def get_hosts_count(cidr):
    return pow(2, 32 - cidr) - 2

def ip_subnet(ip, mask):
    ip_triads = ip.split('.')
    mask_triads = mask.split('.')
    ip_subnet = [
        int(ip_triads[0]) & int(mask_triads[0]),
        int(ip_triads[1]) & int(mask_triads[1]),
	int(ip_triads[2]) & int(mask_triads[2]),
	int(ip_triads[3]) & int(mask_triads[3])
    ]
    return '.'.join(map(str, ip_subnet))


ip = input('Enter IP: ')
mask = int(input('Enter CIDR: '))
class_1 = int(ip.split('.')[0])
if class_1 in range(1, 127):
	print('IP Class: A')
elif class_1 in range(128, 192):
	print('IP Class: B')
elif class_1 in range(192, 224):
	print('IP Class: C')
elif class_1 in range(224, 240):
	print('IP Class: D')
elif class_1 in range(240, 248):
	print('IP Class: E')
ip_mask = cidr_to_netmask(mask)
subnet = ip_subnet(ip, ip_mask)
subnet_ip = ipaddress.IPv4Network(subnet+'/'+str(mask), strict=False)
max_hosts = get_hosts_count(mask)
print(f'Mask: {ip_mask}')
print(f'IP subnet: {subnet}')
print(f'Broadcast Subnet IP: {subnet_ip.broadcast_address}')
print(f'Max hosts: {max_hosts}')
