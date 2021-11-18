## Coins API Documentation

- [Login API](doc/#login-api)
- [Signup API](doc/#signup-api)


## Login API
`POST`: `http://localhost:8000/login/`

#### Headers
```{ Content-type: application/json }```


#### Request Data
```
{
    "email": "User Email",
    "password": "User Password"
}
```

#### Response
```
{
  "status": true,
  "payload": {
  "name": "Rose Hills",
  "email": "rosehills@example.com",
  "password": "somerandompassword",
  "_id": 1,
  "_created": "2021-09-13T12:29:11.474711Z",
  "_updated": "2021-09-13T12:29:11.474711Z",
  "token": "GENERATED_ACCESS_TOKEN"
},
  "message": "Login Api view"
}
```

#### Error Missing Key
```
# Response
{
  "status": false,
  "payload": null,
  "message": "Missing Key 'KEY_NAME' in request data",
  "error": {
    "code": 400
  }
}
```


#### Error Email Does Not Exits ( Email is not present in DB while trying to login )
```
{
  "status": false,
  "payload": null,
  "message": "Email Does not exits",
  "error": {
    "code": 400
  }
}
```

#### Error Password didn't Match
```
{
  "status": false,
  "payload": null,
  "message": "Invalid Password!",
  "error": {
    "code": 400
  }
}
```

<br><br><br>
## Signup API
`POST`: `http://localhost:8000/signup/`

#### Headers
```{ Content-type: application/json }```

#### Request Data
```
{
  "name": "Rose Hills",
  "email": "rosehills@example.com",
  "password": "somerandompassword"
}
```

#### Response
```
{
  "status": true,
  "payload": {
  "name": "Rose Hills",
  "email": "rosehills@example.com",
  "password": "somerandompassword",
  "_id": 1,
  "_created": "2021-09-13T12:29:11.474711Z",
  "_updated": "2021-09-13T12:29:11.474711Z",
  "token": "GENERATED_ACCESS_TOKEN"
},
  "message": "Signup Api view"
}
```

#### Error Missing Key
```
# Response
{
  "status": false,
  "payload": null,
  "message": "Missing Key 'KEY_NAME' in request data",
  "error": {
    "code": 400
  }
}
```

#### Error User Already Exits ( Email is already present in DB while trying to signup )
```
{
  "status": false,
  "payload": null,
  "message": "User already exits, Try login in",
  "error": {
    "code": 400
  }
}
```
<br><br><br>