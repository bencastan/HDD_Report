from fabric.api import *

network_base='.sitesuite.net'
env.user = 'benc'
#env.hosts = ['nfs-01.sitesuite.net', 'proxy-01.sitesuite.net']
env.warn_only=True  # Only warn if erors are encountered, this is to gracefullly close ssh sessions if they timeout
env.roledefs = {
    'proxies':['proxy-01' + network_base, 'proxy-02' + network_base, 'proxy-03'+ network_base, 'proxy-04' + network_base, 'proxy-05' + network_base],
    'app_servers':['app-01' + network_base, 'app-02' + network_base, 'app-03'+ network_base, 'app-04'+ network_base, 'app-05'+ network_base],
    'test':['backup-01' + network_base]
}


def hello():
    print("Hello from fabfile!!!")


@roles('proxies')
def disk_usage():
    run('df')


@roles('proxies')
def inode_usage():
    run('df -i')


@roles('proxies')
def uptime():
    run('uptime')


@roles('proxies')
def version():
    run('cat /etc/issue')


def get_disk_usage(hosts):
    host_list = env.roledefs[hosts]
    return execute(disk_usage, hosts=host_list)


def get_version(hosts):
    host_list = env.roledefs[hosts]
    return execute(version, hosts=host_list)


def get_uptime(hosts):
    host_list = env.roledefs[hosts]
    return execute(uptime, hosts=host_list)


if __name__ == '__main__':
    hello()
    get_version()
    get_uptime()