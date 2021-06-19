<h1 align="center">PyPtero</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.2.5-blue.svg?cacheSeconds=2592000" />
  <a href="https://PyPtero.readthedocs.io" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/Rapi-Dev/PyPtero/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://pypi.org/project/PyPtero" target="_blank">
    <img alt="Pypi" src="https://raster.shields.io/badge/Package-PyPi-informational.svg" />
  </a>
  <a href="https://discord.gg/4haKeuFn" target="_blank">
    <img alt="Discord server" src="https://discord.com/api/guilds/839184636948774963/embed.png" />
  </a>
</p>

> A simple, advanced API wrapper for the Pterodactyl API

### 🏠 [Homepage](https://pyptero.readthedocs.io)

## Key Features
- Ease-of-access
- Includes Everything
- Async And Sync.
- Use of caching allows less requests to the API, Cache is updated everytime you fetch!

## Install

```
Windows
pip install -U https://github.com/Rapi-Dev/PyPtero/

Linux
pip3 install -U https://github.com/Rapi-Dev/PyPtero/
```

## Examples
```py
from PyPtero.Sync import Pterodactyl

client = Pterodactyl(url='My Panel URL', admin_key='My application token')

user = client.users.create(
    username='New-User', password='New-User',
    first_name='Firstname', last_name='Lastname',
    email='some@email.com'
)

user.update(password='Some Super Secret password')
```

## Author

👤 **Daftscientist & Seniatical**

* Website: https://daftscientist.com
* Github: [Daftscientist](https://github.com/Daftscientist) | [Seniatical](https://github.com/Seniatical)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Rapi-Dev/PyPtero/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Daftscientist](https://github.com/Daftscientist) | [Seniatical](https://github.com/Seniatical).<br />
This project is [MIT](https://github.com/Rapi-Dev/PyPtero/blob/main/LICENSE) licensed.
This project is owned by Rapi-Dev (Daftscientist & Saqib).

## Notice
This module is in early works, expect bugs and errors. Were trying to fix any errors which may occasionally popup. 
