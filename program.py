import sys

from fabfile import hello, get_uptime, get_disk_usage, exec_remote_cmd, get_ssl_certs
from fabric.network import disconnect_all
from data import Uptime, Filesystem

alert_high = "90"
alert_med = "75"
alert_low = "50"
final_result = []


def main():
    print_header()
    #Get the data from a host
    #Read the data fropm a host
    #query the data from a host
    #Generate a reoprt
    #Email the report
    #print(hello())


    # try:
    #     print(uptime(get_uptime("nfs")))
    # except:
    #     print("Error! Closing all ssh connections")
    #     disconnect_all()  # close all open ssh connections
    #
    # disconnect_all()  # close all open ssh connections
    #
    #
    # try:
    #     partitions = (disk_usage(get_disk_usage('nfs')))
    #     count = 0
    #     while count < len(partitions):
    #         # Testing for high % utilised filesystems
    #         print(partitions[count])
    #         if str(partitions[count][5])[:-1] > alert_high:
    #             alert_string = (partitions[count][0], partitions[count][6], partitions[count][5])
    #             final_result.append(alert_string)
    #         count += 1
    # except:
    #     print("Error! Closing all ssh connections")
    #     disconnect_all()  # close all open ssh connections
    #
    #
    #
    # print(alert_string)

    try:
        certs = get_ssl_certs('proxy', '202.76.248.141')
        print("Cert == ".format(certs))
        print(type(certs))
        print(certs)

    except:
        print("Error! Closing all ssh connections")
        disconnect_all()  # close all open ssh connections

    disconnect_all()  # close all open ssh connections

def singleton_cmd():
    #disk_usage(host_disk_uage)
    cmd_list =['uptime', 'df']
    for cmd in cmd_list:
        result = exec_remote_cmd(cmd)
        if result.succeeded:
            sys.stdout.write('\n* Command succeeded: ' + cmd+ '\n')
            sys.stdout.write(result+"\n")
        else:
            sys.stdout.write('\n* Command failed: ' + cmd + '\n')
            sys.stdout.write(result + "\n")


def print_header():
    print('------------------------------------')
    print('     HDD CAPACITY Analysing APP')
    print('------------------------------------')
    print


def total_mins(uptimes):
    u = uptimes.split(",")

    # u[0] = '20:54:20 up 110 days' current time, days
    # u[1] = '  1:05' == HH:MM, when added to days * (24 * 60) you get the mins, mind you there is some fiddling to
    #                                   seperate the HH & MM
    # u[2] = '  1 user' == Users - I ignore this one.
    # u[3] = '  load average: 2.11', ' 2.28', ' 2.38' == 5 mins_average, 10 mins_average, 15 mins_average

    host_uptime = u[0].split(" ")
    host_uptime_days = host_uptime[2]
    host_uptime_hours = (int(host_uptime_days) * 24)
    total = (host_uptime_hours * 60 + int(u[1][:-3]) * 60 + int(u[1][-2:]))

    return total


def uptime(host):
    # This needs to load the lines into an array / dictionary and then
    # process it,

    for k,v in host.items():
        hostname = (k)
        uptimes = str((v))
        host_uptime_mins = total_mins(uptimes)

        #print("The host {} has the following uptime {} mins".format(hostname, host_uptime_mins))
    return(host_uptime_mins)





def disk_usage(usage):
    for k, v in usage.items():
        hostname = k
        filesystems = v
        result = []
        filesystem = (filesystems).split("\r\n")
        count_out = 1 # safe to ignore first line as it is the headers
        while count_out < len(filesystem):
            line1 = (filesystem[count_out]).split(",")
            for item in line1:
                (line3) = str(item.split(" "))
                i = (line3).split(" ")
                count_in=0
                filesys_countout = []
                filesys_countout.append(hostname)
                while count_in < len(i):
                    if i[count_in] != "\'\',":
                        filesys_countout.append((i[count_in]).lstrip("\'").rstrip("\',").strip("[\'").rstrip("\']"))
                    count_in += 1
                result.append(filesys_countout)
            count_out += 1
        return result


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
