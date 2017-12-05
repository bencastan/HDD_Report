from fabric.api import *

network_base='.sitesuite.net'
env.user = 'benc'
#env.hosts = ['nfs-01.sitesuite.net', 'proxy-01.sitesuite.net']
env.warn_only=True  # Only warn if erors are encountered, this is to gracefullly close ssh sessions if they timeout
env.roledefs = {
    'proxies':['proxy-01' + network_base, 'proxy-02' + network_base, 'proxy-03'+ network_base, 'proxy-04' + network_base, 'proxy-05' + network_base],
    'proxy':['proxy-01' + network_base],
    'app_servers':['app-01' + network_base, 'app-02' + network_base, 'app-03'+ network_base, 'app-04'+ network_base, 'app-05'+ network_base],
    'test':['backup-01' + network_base],
    'nfs':['nfs-01' + network_base],
    'cpanel':['cpanel' + network_base]


}


def hello():
    print("Hello from fabfile!!!")


@roles('proxies')
def disk_usage():
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        return run('df')


@roles('proxies')
def inode_usage():
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        return run('df -i')


@roles('proxies')
def uptime():
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        return run('uptime')


@roles('proxies')
def version():
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        return run('cat /etc/issue')


@roles('proxies')
def cert_check():
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        print(cmd_string)
        return run('{}'.format(cmd_string))


def get_ssl_certs(host_list, cert_ip):
    host_list = env.roledefs[host_list]
    global cmd_string
    cmd_string = ("'openssl x509 -in /opt/sitesuite/ssl/{}:443.crt -text -noout'".format(cert_ip))
    result = execute(cert_check, hosts=host_list)
    print type(result)
    print("Result == ".format(result))
    return result


def get_disk_usage(host_list):
    host_list = env.roledefs[host_list]
    result = execute(disk_usage, hosts=host_list)
    return result


def get_version(host_list):
    host_list = env.roledefs[host_list]
    result = execute(version, hosts=host_list)
    return result


def get_uptime(host_list):
    host_list = env.roledefs[host_list]
    result = execute(uptime, hosts=host_list)
    return result


def exec_remote_cmd(cmd):
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        return run(cmd)

if __name__ == '__main__':
    hello()
    get_version()
    get_uptime()