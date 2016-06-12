# Introduction

> Grove Indoor Environment Kit for Edison makes it easy to create complete indoor environment applications with Intel Edison and Arduino Breakout Board. With the Base Shield V2, developer can plug up to 11 different Grove sensors & actuators quickly. We provide cool demo code which will be constantly updated, and it will be very easy to operate these sensors & actuators without any programming experience. [Homepage](http://www.seeedstudio.com/wiki/Grove_Indoor_Environment_Kit_for_Edison)

# Audio Setup

```sh
root@edison:~/giekis# cat ~/.asoundrc
pcm.!default {
        type asym
        playback.pcm {
                type plug
                slave.pcm "hw:3,0"
        }
        capture.pcm {
                type plug
                slave.pcm "hw:2,0"
        }
}
```

# Setup Automated

```sh
root@edison:~# curl https://raw.githubusercontent.com/xe1gyq/GiekIs/master/setup.sh -o - | sh
```

# Setup Manual

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
opkg install python-opencv                                                      
```

```sh
root@edison:~/GiekIs# sh requirements.opkg
```

```sh
root@edison:~/GiekIs# cat requirements.pip
requests                                                       
future
python-telegram-bot
pyaudio
wolframalpha
```

```sh
root@edison:~/GiekIs# pip install -r requirements.pip
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

