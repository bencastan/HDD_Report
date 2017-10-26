class Filesystem:
    def __init__(
            self, hostname, path , size, used, avail,
            used_percent, mount):
        self.hostname = hostname
        self.path = path
        self.size = size
        self.used = used
        self.avail = avail
        self.used_percent = used_percent
        self.mount = mount


    @staticmethod
    def create_from_dict(lookup):
        return Filesystem(
            lookup['path'],
            int(lookup['size']),
            int(lookup['used']),
            int(lookup['avail']),
            lookup['mount'],
            int(lookup['used_percent']))


class Uptime:
    def __init__(
        self, hostname, uptime, load5,
            load10, load15):
        self.hostname = hostname
        self.uptime = uptime
        self.load5 = load5
        self.load10 = load10
        self.load16 = load15


    @staticmethod
    def create_from_dict(lookup):
        return Uptime(
            lookup['hostname'],
            lookup['uptime'],
            lookup['load5'],
            lookup['load10'],
            lookup['load15']
        )