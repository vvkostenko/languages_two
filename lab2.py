import re

class IPAddr:
    ip_addr_str = str()
    blocks = list()

    def __init__(self, addr):
        self.ip_addr_str = addr
        self.blocks = re.findall(r'(\d{1,3})' ,addr)

    def __eq__(self, other):
        return isinstance(other, IPAddr) and self.ip_addr_str == other.ip_addr_str

    def __hash__(self):
        return hash(self.ip_addr_str)

    def __lt__(self, other):
        if self.blocks[0] < other.blocks[0]:
            return True

        elif self.blocks[0] == other.blocks[0]:
            if self.blocks[1] < other.blocks[1]:
                return True
            elif self.blocks[1] == other.blocks[1]:
                if self.blocks[2] < other.blocks[2]:
                    return True
                elif self.blocks[2] == other.blocks[2]:
                    if self.blocks[3] < other.blocks[3]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


# Регулярка для нахождения всех ip
ip_regex_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# Получение всех адресов (без дублирующихся)
with open('access.log', 'r') as log_file:
    ip_addrs = list({IPAddr(ip_regex_pattern.match(row).group(0)) for row in log_file})

# Сортировка по подсети \24
ip_addrs.sort()

for i in range (0, ip_addrs.__len__()):
    print(ip_addrs[i].ip_addr_str)