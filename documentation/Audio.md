# Audio

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
