# User Object

An object which represents a user in a pterodactyl server

#### Attributes

`object`(**!pydantic.BaseModel**) - A pydantic model which has all the attributes of a pterodactyl url
> You dont need to directly do `User.object.id` you can just use `User.id` to get the id
`json`(**dict**) - A dictionary which has the raw json which was recieved by the API
`base`(**!PyPtero.API.base.PteroSyncBase**) - An object which is inheritied from your `Application` class
> Used to make certain requests to the API

#### Methods

##### Arguments
