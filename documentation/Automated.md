# Automated

```sh
root@edison:~# curl https://raw.githubusercontent.com/xe1gyq/GiekIs/master/setup.sh -o - | sh
```

__Errors!__

```sh
Collected errors:
 * satisfy_dependencies_for: Cannot satisfy the following dependencies for python-opencv:
 *      python-numpy *
 * opkg_install_cmd: Cannot install package python-opencv.
Unknown package 'mpg123'.
Collected errors:
 * opkg_install_cmd: Cannot install package mpg123.
Unknown package 'fswebcam'.
Collected errors:
 * opkg_install_cmd: Cannot install package fswebcam.
```

```sh
root@edison:~# cd GiekIs/
root@edison:~/GiekIs# 
```