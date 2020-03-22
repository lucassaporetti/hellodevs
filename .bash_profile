# my variables

WORKSPACE='/c/Users/Hugo Saporetti Neto/Workspace/'
PYTHON2_HOME='/c/Python27'
PYTHON3_HOME='/c/Python38'
PYTHON_HOME="$PYTHON3_HOME"

# my aliases 

alias lucas='echo "hellolucas"'
alias reload='unalias -a; clear; source ~/.bash_profile'
alias devs='cd "/c/Users/Hugo Saporetti Neto/Workspace/hellodevs"'
alias np++='"C:\Program Files (x86)\Notepad++\notepad++.exe"'
alias edit='code'
alias python='$PYTHON_HOME/python.exe'
alias python2='$PYTHON2_HOME/python.exe'
alias python3='$PYTHON3_HOME/python.exe'
alias q='exit 0'

# git shortcuts

alias gs='git status'
alias ga='git add'
alias gcm='git commit -m'
alias gpsh='git push'
alias aa='grep alias ~/.bash_profile'

# my paths

PATH="$PYTHON_HOME:$PATH"
