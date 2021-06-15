# Application

All to do with the application side of your pterodactyl server, you will need your ADMIN key for this side!

# Starting
from PyPtero.PyPtero.Sync import Pterodactyl

ptero = Pterodactyl(
    admin_key='Your panels API key',
    url='Your panels URL'
    )
    
#### Arguments
url(str): The url for your panel can include `/api` at the end or not

api_key(typing.Union[list, str]):\
    A list or string for your panels API key\
    If providing a list make sure its in the order of `[client_key, admin_key]`\
    For a string it will become your admin key
    
admin_key(str): The API key for your panel - can be found at `/admin/api`\
client_key(str): The API key for YOUR account - can be found at `/account/api`

use_ssl(bool): Checks if your panel url is following the provided scheme\
               True -> Panel URL must start with `https`\
               False -> Panel URL must start with `http`
               
               Default is `True`
