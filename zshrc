# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=/Users/timothy/.oh-my-zsh

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

alias fucking=sudo

# Setting PATH for Python 2.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"
export PATH

POWERLEVEL9K_MODE="nerdfont-complete"

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="powerlevel9k/powerlevel9k"

# Set list of themes to load
# Setting this variable when ZSH_THEME=random
# cause zsh load theme from this variable instead of
# looking in ~/.oh-my-zsh/themes/
# An empty array have no effect
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  zsh-autosuggestions
)

source $ZSH/oh-my-zsh.sh
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nano'
else
  export EDITOR='nano'
fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
export SSH_KEY_PATH="~/.ssh/do_tlkh"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

#POWERLEVEL9K_PROMPT_ON_NEWLINE=true
#POWERLEVEL9K_PROMPT_ADD_NEWLINE=true

POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=''
POWERLEVEL9K_MULTILINE_SECOND_PROMPT_PREFIX=''

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context dir newline vcs status dir_writable)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(root_indicator command_execution_time time)

# Context
DEFAULT_USER="timothy"
POWERLEVEL9K_ALWAYS_SHOW_CONTEXT=true
POWERLEVEL9K_CONTEXT_DEFAULT_FOREGROUND='white'
POWERLEVEL9K_CONTEXT_DEFAULT_BACKGROUND='blue'
POWERLEVEL9K_CONTEXT_TEMPLATE="%F{white}%n%f"

# Dirs
POWERLEVEL9K_DIR_HOME_BACKGROUND='blue'
POWERLEVEL9K_DIR_HOME_FOREGROUND='black'
POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND='blue'
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND='black'
POWERLEVEL9K_DIR_DEFAULT_BACKGROUND='yellow'
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND='black'
#POWERLEVEL9K_SHORTEN_DIR_LENGTH=3
#POWERLEVEL9K_SHORTEN_STRATEGY="truncate_from_right"

# VCS colours
POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='yellow'
POWERLEVEL9K_VCS_MODIFIED_FOREGROUND='white'
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='red'
POWERLEVEL9K_VCS_UNTRACKED_FOREGROUND='white'
POWERLEVEL9K_VCS_CLEAN_BACKGROUND='green'
POWERLEVEL9K_VCS_CLEAN_FOREGROUND='white'

# VCS CONFIG
POWERLEVEL9K_SHOW_CHANGESET=true

# Status
POWERLEVEL9K_OK_ICON=$'\uf109'
POWERLEVEL9K_FAIL_ICON=$'\uf165'
POWERLEVEL9K_CARRIAGE_RETURN_ICON=$'\uf165'
POWERLEVEL9K_STATUS_OK_FOREGROUND='black'
POWERLEVEL9K_STATUS_OK_BACKGROUND='white'

# VCS icons
POWERLEVEL9K_VCS_GIT_ICON=$'\uf1d3'
POWERLEVEL9K_VCS_GIT_GITHUB_ICON=$'\uf113'
POWERLEVEL9K_VCS_STAGED_ICON=$'\uf055'
POWERLEVEL9K_VCS_UNSTAGED_ICON=$'\uf071'
POWERLEVEL9K_VCS_UNTRACKED_ICON=$'\uf00d'
POWERLEVEL9K_VCS_INCOMING_CHANGES_ICON=$'\uf0ab '
POWERLEVEL9K_VCS_OUTGOING_CHANGES_ICON=$'\uf0aa '

POWERLEVEL9K_COMMAND_EXECUTION_TIME_FOREGROUND="$DEFAULT_BACKGROUND"
POWERLEVEL9K_COMMAND_EXECUTION_TIME_BACKGROUND="$DEFAULT_FOREGROUND"
POWERLEVEL9K_EXECUTION_TIME_ICON="\uf253"
POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD="1"

# Time
POWERLEVEL9K_TIME_FORMAT="%F{black}\uf017 %D{%I:%M}%f"
POWERLEVEL9K_TIME_BACKGROUND='white'
POWERLEVEL9K_TIME_FOREGROUND='black'

# zsh-syntax-highlighting
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)
ZSH_HIGHLIGHT_PATTERNS+=("rm -rf *" "fg=white,bold,bg=red")
typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[path]="fg=white"
ZSH_HIGHLIGHT_STYLES[path_pathseparator]="fg=grey"
ZSH_HIGHLIGHT_STYLES[alias]="fg=cyan"
ZSH_HIGHLIGHT_STYLES[builtin]="fg=cyan"
ZSH_HIGHLIGHT_STYLES[function]="fg=cyan"
ZSH_HIGHLIGHT_STYLES[command]="fg=green"
ZSH_HIGHLIGHT_STYLES[precommand]="fg=green"
ZSH_HIGHLIGHT_STYLES[hashed-command]="fg=green"
ZSH_HIGHLIGHT_STYLES[commandseparator]="fg=yellow"
ZSH_HIGHLIGHT_STYLES[redirection]="fg=magenta"
ZSH_HIGHLIGHT_STYLES[bracket-level-1]="fg=cyan,bold"
ZSH_HIGHLIGHT_STYLES[bracket-level-2]="fg=green,bold"
ZSH_HIGHLIGHT_STYLES[bracket-level-3]="fg=magenta,bold"
ZSH_HIGHLIGHT_STYLES[bracket-level-4]="fg=yellow,bold"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/timothy/Downloads/google-cloud-sdk/path.zsh.inc' ]; then source '/Users/timothy/Downloads/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/timothy/Downloads/google-cloud-sdk/completion.zsh.inc' ]; then source '/Users/timothy/Downloads/google-cloud-sdk/completion.zsh.inc'; fi
