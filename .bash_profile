#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ !$DISPLAY && $XDG_VTNR -eq 1 ]]; then
	exec startx
fi

export LANG=en_US.UTF-8
export LANG=pt_BR.UTF-8
export TERM=rxvt-unicode
