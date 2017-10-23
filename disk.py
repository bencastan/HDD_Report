class filesystem:
    def __init__(
            self,path , size, uesd, avail,
            used_percent, mount):
        self.path = path
        self.size = size
        self.used = avail
        self.used_percent = used_percent
        self.mount = mount


    @staticmethod
    def create_from_dict(lookup):
        return filesystem(
            lookup['path'],
            int(lookup['size']),
            int(lookup['used']),
            int(lookup['avail']),
            lookup['mount'],
            int(lookup['used_percent']))