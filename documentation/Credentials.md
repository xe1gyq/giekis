# Credentials

```sh
root@edison:~/GiekIs# nano core/configuration/credentials.config
```

```sh
[twitter]
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
  

[voicerss]
apikey = 

[mashape]
mashapekey = 

[wolframalpha]
appid = 

[google]
api_key = 
    
[gmail]
username = 
password = 
    
[telegram]
token = 

[wit]
accesstoken=

# End of File
```

```sh
root@edison:~/GiekIs# nano core/configuration/voicerss.ak

[Write Voicerss ApiKey]

```

```sh
root@edison:~/GiekIs# nano core/configuration/voicerss.mk

[Write Mashape MashapeKey]

```

```sh
root@edison:~/GiekIs# ls core/configuration/
credentials.config  haarcascade_frontalface_alt.xml  voicerss.ak  voicerss.mk
```

## Google Credentials

```sh
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
```
