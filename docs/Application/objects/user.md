# User Object

An object which represents a user in a pterodactyl server

#### Attributes

`object`(**!pydantic.BaseModel**) - A pydantic model which has all the attributes of a pterodactyl url
> You dont need to directly do `User.object.id` you can just use `User.id` to get the id
`json`(**dict**) - A dictionary which has the raw json which was recieved by the API
`base`(**!PyPtero.API.base.PteroSyncBase**) - An object which is inheritied from your `Application` class
> Used to make certain requests to the API

#### Methods

##### Update - `User.update(**attrs)`
> Updates a pterodactyl user with the provided attributes

**Example**
```py
from PyPtero.Sync import Pterodactyl

client = Pterodactyl(url='My Panel URL', admin_key='My application token')
user = client.fetch_user(10)

user = user.update(password='Some Super Secret Password')
```

###### Returns
A new user object with the updated attributes

###### Arguments
email(**str**) - Update the email for the user\
username(**str**) - Update the username for the user\
first_name(**str**) - Update the first name for the user\
last_name(**str**) - Update the last name for the user\
language(**str**) - Update the language for the user\
password(**str**) - Update the password for the user\
external_id(**str**) - Update the external ID for the user\
root_admin(**bool**) - Update root admin status for the user

##### Copy - `User.copy()`
> Returns a user new user object which is identical to your current user

**Example**
```py
from PyPtero.Sync import Pterodactyl

client = Pterodactyl(url='My Panel URL', admin_key='My application token')
user = client.fetch_user(10)

seperate_user_object = user.copy()
```

###### Returns
A new user object

##### Delete - `User.delete()`
> Delete a user from your pterodactyl panel

**Example**
```py
from PyPtero.Sync import Pterodactyl

client = Pterodactyl(url='My Panel URL', admin_key='My application token')
user = client.fetch_user(10)

user.delete()
```

###### Returns
True if it has worked else it will raise an error
