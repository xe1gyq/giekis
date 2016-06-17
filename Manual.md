# Manual

```sh
root@edison:~# git clone https://github.com/xe1gyq/GiekIs.git
Cloning into 'GiekIs'...
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
Checking connectivity... done.
root@edison:~# 
```

```sh
root@edison:~# cd GiekIs/
root@edison:~/GiekIs# 
```

```sh
root@edison:~/GiekIs# cat requirements.opkg
opkg install python-dev 
opkg install python-opencv
opkg install libxft-dev
opkg install libpng-dev
opkg install libjpeg-dev
opkg install alsa-utils 
opkg install libjack
opkg install --nodeps jack-dev 
opkg install libportaudio-dev
opkg install flac-dev
opkg install espeak 
opkg install mpg123
opkg install fswebcam
```

```sh
root@edison:~/GiekIs# sh requirements.opkg
...
root@edison:~/GiekIs# 
```

```sh
root@edison:~/GiekIs# cat requirements.pip
requests
future
python-telegram-bot
wolframalpha
pyaudio
twython
SpeechRecognition
google-api-python-client
```

```sh
root@edison:~/GiekIs# pip install -r requirements.pip
...
root@edison:~/GiekIs# 
```

[Core](https://xe1gyq.gitbooks.io/core/content/)

```sh
root@edison:~/GiekIs# git clone https://github.com/xe1gyq/core.git
Cloning into 'core'...
remote: Counting objects: 1109, done.
remote: Compressing objects: 100% (171/171), done.
remote: Total 1109 (delta 93), reused 0 (delta 0), pack-reused 924
Receiving objects: 100% (1109/1109), 217.79 KiB | 0 bytes/s, done.
Resolving deltas: 100% (605/605), done.
Checking connectivity... done.
root@edison:~/GiekIs#
```

```sh
root@edison:~/GiekIs# ls
LICENSE    SUMMARY.md  documentation  main.py            requirements.pip
README.md  core        examples       requirements.opkg  setup.sh
root@edison:~/GiekIs# 
```