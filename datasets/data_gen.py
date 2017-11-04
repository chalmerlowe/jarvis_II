# data generator

# The first column is an IP address. IP-Address (1)
# The second column is an IP address. IP-Address (2)
# The third column is the protocol.  In this case the protocol is set to 6 (TCP)
# The fourth column is the port associated with IP-Address 1.  In this case Ephemeral Ports.
# The fifth column is the port associated with IP-Address 2.  In this case HTTPS (443).
# The sixth column is the number of bytes received by IP-Address 1.
# The seventh column is the number of bytes received by IP-Address 2.
# The eighth column is the number of packets received by IP-Address 1.
# The ninth column is the number of packets received by IP-Address 2.
# The tenth column is the time the first packet was received.
# The eleventh column is the time the last packet was received.
# The twelfth column shows which IP Address sent the first packet (initiated the conversation).
# The thirteenth column shows which IP Address sent the last packet (finished the conversation).

from random import choice, shuffle, sample, randint
from datetime import datetime, timedelta
from ipaddress import ip_address as ipaddr, ip_network as ip_netw

# CONFIGURATION SETTINGS
num_of_lines = 210000
num_of_ips = 30
num_of_netw = 10

num_of_target_src_ips = 1
num_of_target_dst_ips = 1
num_of_target_src_netw = 1
num_of_target_dst_netw = 1

out_file = 'output.csv'

fout = open(out_file, 'w')

def generate_ips(num_of_netw=num_of_netw, num_of_ips=num_of_ips):
    '''creates a set of networks and chooses a random set of ip addresses from
    each network.
    '''

    subnets = ['/23', '/24', '/25', '/26']
    ips_per_netw = round(num_of_ips / num_of_netw)
    octets = []
    ips = []

    # create a set of ips for each of the networks
    for x in range(num_of_netw):
        # create ips based on four octets
        for octet in range(4):
            octets.append(str(choice(range(1, 256))))

        ip = '.'.join(octets)
        octets = []

        # generate an ipaddress.ip_network based on the
        #     ipaddress created above
        network = ip_netw(ip + choice(subnets), strict=False)

        # create a random number of ips per network
        for x in range(ips_per_netw + choice([0, 1, 1, 1, 2, 2, 3])):

            # choose a random ip from the network
            ips.append(str(choice(list(network))))
            if len(ips) == num_of_ips:
                break
    return ips

def protocol_gen():
    '''Generate a random protocol value based on the following options:

Internet Control Message Protocol (ICMP): 1
Transmission Control Protocol (TCP): 6
Exterior Gateway Protocol (EGP): 8
User Datagram Protocol (UDP): 17
Reliable Datagram Protocol (RDP): 27
Encapsulation Security Payload (ESP) IPSec: 50
Authentication Header (AH) IPSec: 51
OSPF Open Shortest Path First: 89'''

    protocols = [1, 6, 8, 17, 27, 50, 51, 89]
    return choice(protocols)

def port_gen(common=True, ephemeral=True):
    '''Generate a random port value between 0 and 65535, depending upon whether
    common OR ephemeral is set to True.

    if common = True, returns a port from this list:
        21: File Transfer Protocol (FTP)
        22: Secure Shell (SSH)
        23: Telnet remote login service
        25: Simple Mail Transfer Protocol (SMTP)
        53: Domain Name System (DNS) service
        80: Hypertext Transfer Protocol (HTTP) used in the World Wide Web
        110: Post Office Protocol (POP3)
        123: Network Time Protocol (NTP)
        143: Internet Message Access Protocol (IMAP)
        161: Simple Network Management Protocol (SNMP)
        194: Internet Relay Chat (IRC)
        443: HTTP Secure (HTTPS)
    if ephemeral = True, returns a port between 1024 and 65535
    '''

    if common:
        return choice([21, 22, 23, 25, 53, 80, 110, 123, 143, 161, 194, 443])
    elif ephemeral:
        return randint(1024, 65535)

def bytes_gen():
    return randint(0, 550000000)

def packets_gen(target=False):
    if target == True:
        return choice([14, 16])
    return randint(0, 710000)


rng = 700
starttime = datetime.now()
current_time = starttime

# Cycletime represents the beacon time (i.e. 5 min/300 seconds)
cycletime = starttime - timedelta(0, 300)
# minimum_delta represents the time between rows
minimum_delta = timedelta(0, 0, 200000)
# micro_second_options >>> the diffs between first time and last time
micro_second_options = list(range(10000, 6000000, 12343))


ms_range = list(range(100000, 200000))


def create_tdelta(ms_range):            # rename...
    '''creates a timedelta that falls between the upper and lower bounds
    within the sequence ms_range
    Essentially sets the differential between rows....
    '''

    return timedelta(0, 0, choice(ms_range))

# for ts in range(rng):

def initiator_gen(target=False):
    flags = [(1, 1), (1, 2), (2, 1), (2, 2)]
    if target == True:
        return (1, 1)
    return choice(flags)


# Create lists of IPs and target IPs
'''
num_of_target_src_ips = 2
num_of_target_dst_ips = 2
num_of_target_src_netw = 1
num_of_target_dst_netw = 1
'''

ip_list_src = generate_ips()
shuffle(ip_list_src)
ip_list_src_target = generate_ips(num_of_netw=num_of_target_src_netw, num_of_ips=num_of_target_src_ips)
shuffle(ip_list_src_target)

ip_list_dest = generate_ips()
shuffle(ip_list_dest)
ip_list_dest_target = generate_ips(num_of_netw=num_of_target_dst_netw, num_of_ips=num_of_target_dst_ips)
shuffle(ip_list_dest_target)


for line in range(num_of_lines):
    current_time -= create_tdelta(ms_range)
    target_cycle = current_time - cycletime < minimum_delta
    if target_cycle:
        cycletime = current_time - timedelta(0, 300)
        # inject the good target stuff...
        # periodicity

        # bytes/packets
        packets1 = str(packets_gen(True))
        packets2 = str(packets_gen(True))

        # ip pairs
        ip1 = choice(ip_list_src_target)
        ip2 = choice(ip_list_dest_target)

        # packet sources
        packet_src = initiator_gen(True)

    else:
        # the regular stuff
        # bytes/packets
        packets1 = str(packets_gen(False))
        packets2 = str(packets_gen(False))

        # ip pairs
        ip1 = choice(ip_list_src)
        ip2 = choice(ip_list_dest)

        # packet sources
        packet_src = initiator_gen(False)

    protocol = str(protocol_gen())
    args = [True, False]
    shuffle(args)
    common, ephemeral = args
    port1 = str(port_gen(common, ephemeral))
    common, ephemeral = ephemeral, common
    port2 = str(port_gen(common, ephemeral))
    bytes1 = str(bytes_gen())
    bytes2 = str(bytes_gen())


    time_first = current_time

    # Set the time difference ... using micro_second_options
    time_last = time_first + timedelta(0, 0, choice(micro_second_options))
    time_first = datetime.strftime(time_first, '%Y-%m-%d-%H:%M:%S.%f')
    # time_last = str(time_last)
    time_last = datetime.strftime(time_last, '%Y-%m-%d-%H:%M:%S.%f')
    first_packet = str(packet_src[0])
    last_packet = str(packet_src[1])

    output = ' '.join([ip1, ip2, protocol, port1, port2,
          bytes1, bytes2, packets1, packets2,
          time_first, time_last, first_packet, last_packet]) + '\n'
    fout.write(output)
    # if target_cycle:
    #     print(ip1, ip2, protocol, port1, port2,
    #           bytes1, bytes2, packets1, packets2,
    #           time_first, time_last, first_packet, last_packet)
    # else:
    #     print(ip1, ip2, protocol, port1, port2,
    #           bytes1, bytes2, packets1, packets2,
    #           time_first, time_last, first_packet, last_packet)

# QUESTIONS/TODO:
# Redefine the target cycle to make it tighter AND to ensure
# that it is focused on only one IP pair
# and so that the indicators are stronger
