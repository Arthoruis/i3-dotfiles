#!/bin/sh
# ~/.xinitrc - generated for i3 on Arch Linux (user: arthorius)
# Starts gnome-keyring in the session D-Bus and then execs i3

# Load system and user X resources
userresources=$HOME/.Xdefaults
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

DEFAULT_SESSION='i3 --shmlog-size 0'

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# Run scripts in /etc/X11/xinit/xinitrc.d
if [ -d /etc/X11/xinit/xinitrc.d ] ; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
        [ -x "$f" ] && . "$f"
    done
    unset f
fi

# Start gnome-keyring on the session D-Bus (important: start before i3)
# This ensures org.freedesktop.secrets is registered on the correct DBus
if command -v gnome-keyring-daemon >/dev/null 2>&1; then
    eval "$(gnome-keyring-daemon --start --components=secrets,ssh,gpg)"
    export SSH_AUTH_SOCK
    export GPG_AGENT_INFO
    export GNOME_KEYRING_CONTROL
    export GNOME_KEYRING_PID
fi

# Disable bell and power saving (keep these here; they run before exec)
xset b off
xset -dpms
xset s off

# Start i3 without dbus-launch so it uses the same session DBUS
exec i3 --shmlog-size 0
