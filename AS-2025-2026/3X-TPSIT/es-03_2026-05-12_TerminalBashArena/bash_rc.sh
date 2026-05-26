case $- in
	*i*) ;;
	*) return;;
esac

shopt -s histappend
shopt -s checkwinsize
shopt -s cdspell
shopt -s autocd
shopt -s globstar

HISTCONTROL=ignoreboth:erasedups
HISTIGNORE="ls:ls -*:cd:cd -:pwd:exit:date:history"
HISTSIZE=1000
HISTFILESIZE=2000
PROMPT_COMMAND="history -a; history -c; history -r; $PROMPT_COMMAND"

if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
	debian_chroot=$(cat /etc/debian_chroot)
fi

force_color_prompt=yes
if [ -n "$force_color_prompt" ]; then
	if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
		color_prompt=yes
	else
		color_prompt=
	fi
fi

if [ "$color_prompt" = yes ]; then
	if [ "$EUID" -eq 0 ]; then
		# ROOT -> Red color
		PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w #\[\033[00m\] '
	else
		# User -> Cyan color
		PS1='${debian_chroot:+($debian_chroot)}\[\033[01;36m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w \$\[\033[00m\] '
	fi
else
	PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

case "$TERM" in
xterm*|rxvt*)
	PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
	;;
esac

if [ -x /usr/bin/dircolors ]; then
	test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
	alias ls='ls -hvF --color=auto --group-directories-first --time-style=long-iso'
	alias grep='grep --color=auto'
	alias fgrep='fgrep --color=auto'
	alias egrep='egrep --color=auto'
fi

alias vi='nvim'
alias vim='nvim'
alias oldvim='nvim'
alias nano='nano -l -T 4'

if [ -f ~/.bash_aliases ]; then
	. ~/.bash_aliases
fi

if ! shopt -oq posix; then
	if [ -f /usr/share/bash-completion/bash_completion ]; then
		. /usr/share/bash-completion/bash_completion
	elif [ -f /etc/bash_completion ]; then
		. /etc/bash_completion
	fi
fi