from napalm import get_network_driver
import json

driver = get_network_driver('ios')
st1 = {'secret' : 'vishal'}
device = driver('10.110.161.20', 'vishal', 'vishal', optional_args=st1)
device.open()

arp_output = device.get_arp_table()
for element in arp_output:
    del element['interface']
print('Output of show arp'+ '\n')
new1 = (json.dumps(arp_output, sort_keys=True, indent=4))
print(new1)
save_file = open("arp.txt", "w")
save_file.write(new1)
save_file.close()

ping_output = device.ping(destination='10.10.1.6')
ping_output1 = [ping_output.get('success') for d in ping_output]
for element in ping_output1:
    del element['results']
    del element['probes_sent']
    del element['rtt_stddev']
    del element['packet_loss']
print('Output of ping to R3 fa1/1'+ '\n')
new2 = (json.dumps(ping_output1, sort_keys=True, indent=4))
print(new2)
save_file = open("ping.txt", "w")
save_file.write(new2)
save_file.close()
device.close()
