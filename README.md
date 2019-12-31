# Aavishkar Games

This is the official repository of the games developed for the aavishkar app by GLUG.

## Games

- Close the Box (CTB)
- 21 Card Strategy Game (TO)

## Twenty One API Documentation

### POST /start

Request Body:  
```
{  
    "player": String
}
```
Response Body:
```
{
    "id": String,
    "players": [ String ],
    "currentmove": String,
    "gamedata": [
        {
            "player": String,
            "cards" : [ String ],
            "score" : Integer
        }   
    ],
    "currentmove": String
}
```

### POST /join/{sessionId}

Request Body:
```
{
    "player": String
}
```
Response Body:
```
"id": String,
    "players": [ String ],
    "currentmove": String,
    "gamedata": [
        {
            "player": String,
            "cards" : [ String ],
            "score" : Integer
        }   
    ],
    "currentmove": String
```

### POST /hit/{sessionId}

Request Body:
```
{
    "player": String
}
```
Response Body:
```
"id": String,
    "players": [ String ],
    "currentmove": String,
    "gamedata": [
        {
            "player": String,
            "cards" : [ String ],
            "score" : Integer
        }   
    ],
    "currentmove": String
```

### POST /stand/{sessionId}

Request Body:
```
{
    "player": String
}
```
Response Body:
```
"id": String,
    "players": [ String ],
    "currentmove": String,
    "gamedata": [
        {
            "player": String,
            "cards" : [ String ],
            "score" : Integer
        }   
    ],
    "currentmove": String
```
