from fabfile import hello, get_uptime, get_disk_usage
from fabric.network import disconnect_all

network_base='.sitesuite.net'
#env.user = 'benc'

#env.roledefs = {
#    'proxies':['proxy-01' + network_base, 'proxy-02' + network_base, 'proxy-03'+ network_base, 'proxy-04' + network_base, 'proxy-05' + network_base],
#    'app_servers':['app-01' + network_base, 'app-02' + network_base, 'app-03'+ network_base, 'app-04'+ network_base, 'app-05'+ network_base]
#}

def main():
    print_header()
    #Get the data from a host
    #Read the data fropm a host
    #query the data froma host
    #Generate a reoprt
    #Email the report
    #print(hello())
    try:
        host_uptime = {}
        host_uptime=(get_uptime("test"))
        #host_disk_uage=(get_disk_usage('proxies'))
    except:
        print("Error! Closing all ssh connections")
        disconnect_all()  # close all open ssh connections

    disconnect_all()  # close all open ssh connections

    print("I am {} ".format(host_uptime))
    uptime(host_uptime)


def print_header():
    print('------------------------------------')
    print('     HDD CAPACITY Analysing APP')
    print('------------------------------------')
    print()


def uptime(host):
    # This needs to load the lines into an array / dictionary and then
    # process it, We will want the 3rd line only. and it will need some splitting
    print
    print
    print(type(host))
    print(host)


if __name__ == '__main__':
    main()


# Fabric output:

# [proxy-05.sitesuite.net] Executing task 'uptime'
# [proxy-05.sitesuite.net] run: uptime
# [proxy-05.sitesuite.net] out:  12:02:47 up 5 days,  1:46,  2 users,  load average: 16.30, 6.23, 3.21
# [proxy-05.sitesuite.net] out:
#
# [proxy-05.sitesuite.net] Executing task 'disk_usage'
# [proxy-05.sitesuite.net] run: df
# [proxy-05.sitesuite.net] out: Filesystem     1K-blocks     Used Available Use% Mounted on
# [proxy-05.sitesuite.net] out: /dev/vda1       16689020 12737892   3080320  81% /
# [proxy-05.sitesuite.net] out: udev               10240        0     10240   0% /dev
# [proxy-05.sitesuite.net] out: tmpfs             812172     8556    803616   2% /run
# [proxy-05.sitesuite.net] out: tmpfs            2030420        0   2030420   0% /dev/shm
# [proxy-05.sitesuite.net] out: tmpfs               5120        0      5120   0% /run/lock
# [proxy-05.sitesuite.net] out: tmpfs            2030420        0   2030420   0% /sys/fs/cgroup
# [proxy-05.sitesuite.net] out:



# #Sample Data
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/vda1        31G   15G   15G  50% /
# udev             10M     0   10M   0% /dev
# tmpfs           403M   41M  362M  11% /run
# tmpfs          1006M     0 1006M   0% /dev/shm
# tmpfs           5.0M     0  5.0M   0% /run/lock
# tmpfs          1006M     0 1006M   0% /sys/fs/cgroup
