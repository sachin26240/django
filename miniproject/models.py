from django.db import models

# Create your models here.


class Addressing:
    def __init__(self, ip, block, ipx):
        self.ip = ip
        self.block = block
        self.ipx = ipx
        self.netId = int(ip.split('.')[0])
        self.hint = [0, 0, 0, 0, 0]

    def className(self):
        if (self.netId < 128):
            self.hint[0] = 'It is the Class with left most octet between (and including) 0 and 127'
            return "Class A"
        elif (self.netId < 192):
            self.hint[0] = 'The left most octet is between (and including) 128 and 191'
            return "Class B"
        elif (self.netId < 224):
            self.hint[0] = 'The left most octet is between (and including) 192 and 223'
            return "Class C"
        elif (self.netId < 240):
            return "Class D"
        elif (self.netId < 256):
            return "Class E"
        else:
            return "Invalid"

    def subnet(self):
        if (self.netId < 128):
            sub = int(self.block)-8
            subnet = 2 ** sub
            self.hint[1] = 'Number of Subnets = 2^(n-8), where n is the network bit'
            return subnet
        elif (self.netId < 192):
            sub = int(self.block)-16
            subnet = 2 ** sub
            self.hint[1] = 'Number of Subnets = 2^(n-16), where n is the network bit'
            return subnet
        elif (self.netId < 224):
            sub = int(self.block)-24
            subnet = 2 ** sub
            self.hint[1] = 'Number of Subnets = 2^(n-24), where n is the network bit'
            return subnet

    def host(self):
        host_bit = 32-int(self.block)
        host = (2 ** host_bit)-2
        self.hint[2] = 'Number of Hosts = 2^(32-n)-2, where n is the network bit'
        return host

    def mask(self):
        block = int(self.block)
        mask = str(1)
        for i in range(1, block):
            mask = mask+str(1)

        for i in range(32-block):
            mask = mask+str(0)

        ip1 = mask[0:8]
        ip2 = mask[8:16]
        ip3 = mask[16:24]
        ip4 = mask[24:32]

        ip11 = str(self.BinaryToDecimal(ip1))
        ip22 = str(self.BinaryToDecimal(ip2))
        ip33 = str(self.BinaryToDecimal(ip3))
        ip44 = str(self.BinaryToDecimal(ip4))

        subnetmask = ip11 + '.' + ip22 + '.' + ip33 + '.' + ip44
        self.hint[3] = 'Subnet mask is '+subnetmask
        return subnetmask

    def BinaryToDecimal(self, binary):
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        return decimal

    def IpCompare(self):
        hostpersubnet = self.host()+2
        x = int(self.ip.split('.')[-1])//hostpersubnet
        hostId = x*hostpersubnet
        brodId = hostId+hostpersubnet-1
        if((int(self.ipx) < brodId) and (int(self.ipx) > hostId)):
            self.hint[4] = 'Both IP addresses are in Same Network'
            return "YES"
        else:
            self.hint[4] = 'Both IP addresses are not in Same Network'
            return "NO"

    def hints(self):
        hint = self.hint
        return hint
