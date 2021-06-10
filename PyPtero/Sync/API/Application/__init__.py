from . import *
from ..base import PteroSyncBase
from ....exceptions import *
import typing
from .users import Users

@typing.final
class Application(PteroSyncBase):
    def __init__(self, pterodactyl) -> None:
        self.key = pterodactyl.admin_key
        self.session = pterodactyl.session
        self.url = pterodactyl.url

        if not self.key:
            MissingAPIKey('Cannot resolve a valid API key, Please visit `%s/admin/api`' % self.url)

        super().__init__(
            api_token=self.key,
            url=self.url,
            session=self.session
        )

        self.users = Users(pterodactyl)