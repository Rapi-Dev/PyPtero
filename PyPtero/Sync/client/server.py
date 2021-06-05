class Server(object):
    def __init__(self, pterodactyl: object) -> None:
        self.domain = pterodactyl.domain
        self.api_key = pterodactyl.api_key