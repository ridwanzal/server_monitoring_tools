import socket, time, json, datetime, platform, psutil, requests, pprint, uuid, os
import shutil
from subprocess import call


def main():
    #hostname info5
    hostname = socket.gethostname()
    print "Hostname : ", hostname 
    
    #cpu info
    cpu_count = psutil.cpu_count()
    cpu_usage = psutil.cpu_percent()
    print "CPU: tCount : ", cpu_count, " tUsage:", cpu_usage
    
    #memory info
    memory_stats = psutil.virtual_memory()
    memory_total = memory_stats.total
    memory_used = memory_stats.used
    memory_used_percent = memory_stats.percent
    print "Memory : Percentage : ", memory_used_percent, "%" ,  " Total:", memory_total / 1e+6/1000, "GB", " Used:", memory_used / 1e+6//1000, "GB"
    
    #platform info
    system = {
            "name" : platform.system(),
            "version" : platform.release(),
            "codename" : platform.linux_distribution()
    }
    print "OS :", system["name"], system["codename"]
    
    
    #storage information
    disk_info = psutil.disk_usage('/');
    print "Disk Usage: ", disk_info.percent, "%" 
    print "Bandwith : ", bandwidth()
    
def bandwidth() :
     # Get net in/out
    net1_out = psutil.net_io_counters().bytes_sent
    net1_in = psutil.net_io_counters().bytes_recv

    # Get new net in/out5
    net2_out = psutil.net_io_counters().bytes_sent
    net2_in = psutil.net_io_counters().bytes_recv

    # Compare and get current speed
    if net1_in > net2_in:
        current_in = 0
    else:
        current_in = net2_in - net1_in
    
    if net1_out > net2_out:
        current_out = 0
    else:
        current_out = net2_out - net1_out
    
    network = "traffic_in", current_in, "traffic_out", current_out
    return network

while True:
    main()
    time.sleep(1)
    os.system('clear')  
