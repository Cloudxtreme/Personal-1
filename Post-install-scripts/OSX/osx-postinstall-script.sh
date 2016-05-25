#! /bin/bash

# Post Install Script for my iMac

#if [ "$(id -u)" != "0" ]; then
#  echo "Sorry, you are not root."
#  exit 1
#fi

# Check for Homebrew,
# Install if we don't have it
which -s brew
if [[ $? != 0 ]] ; then
  echo "Installing homebrew..."
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else

# Install GNU `find`, `locate`, `updatedb`, and `xargs`, g-prefixed
echo "export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"" >> ~/.bash_profile
brew install findutils

# Install more recent versions of some OS X tools
brew tap homebrew/dupes
brew install homebrew/dupes/grep

# Installs brews
brews=(
  bash
  tree
  python
  htop
  git
  wget
  mackup
  libdvdcss
  openconnect
  watch
  rsync
  openssh
  less
  argon/mas/mas
  )

brew install ${brews[@]}

# Caskroom
echo "-----> Installing Caskroom"
brew install caskroom/cask/brew-cask

# Apps
apps=(
  1password
  alfred
  appcleaner
  atom
  bartender
  dockertoolbox
  dropbox
  evernote
  google-chrome
  launchcontrol
  istat-menus
  iterm2
  path-finder
  remote-desktop-manager
  sonos
  superduper
  quicklook-json
  vagrant
  )

  # Install apps to /Applications
  # Default is: /Users/$user/Applications
echo "-----> installing apps..."
brew cask install --appdir="/Applications" ${apps[@]}

# Fix Alfred path
brew cask alfred link

# Use Cask to install fonts
brew tap caskroom/fonts

# Fonts
fonts=(
  font-ubuntu
  font-ubuntu-mono-powerline
  font-source-code-pro
  font-inconsolata-dz
  font-dejavu-sans
  font-dejavu-sans-mono-for-powerline
  font-cousine
  font-comic-neue
  font-anonymous-pro
  )

# install fonts
echo "-----> installing fonts..."
brew cask install ${fonts[@]}

# use MAS to install Mac App Store software
mas signin adam@revolutionphotos.com "CuIeyy7j!!"
masapps=(
494803304 #WiFi Explorer
425424353 #The Unarchiver
422293948 #IP Scanner Home
425955336 #Skitch
411246225 #Caffeine
413965349 #Soulver
1055511498 #Day One
866773894 #Quiver
634108295 #Acorn
557168941 #Tweetbot
448003584 #Simplify
409201541 #Pages
880001334 #Reeder
450201424 #Lingon 3
715768417 #MicrosoftRemoteDesktop
877479749 #powershot
412529613 #Cinch
409203825 #Numbers
445189367 #PopClip
)

mas install ${masapps[@a]}

# git

mkdir /Users/adamschoonover/Git
cd /Users/adamschoonover/Git/
git clone git@github.com:nonstopflights/Personal.git

brew cleanups


read HOSTNAME
echo "Choose a hostname:"
## SET HOSTNAME IN ALL THE RIGHT PLACES
sudo scutil --set ComputerName $HOSTNAME
sudo scutil --set HostName $HOSTNAME
sudo scutil --set LocalHostName $HOSTNAME
sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string $HOSTNAME

## TURN OFF SCREENSAVER PASSWORD DELAY
echo "-----> Change screen saver password delay"
defaults write com.apple.screensaver askForPassword -int 1
defaults write com.apple.screensaver askForPasswordDelay -int 0

## DISABLE NATURAL SCROLLING
echo "-----> Change Natural Scroll Direction"
defaults write NSGlobalDomain com.apple.swipescrolldirection -bool false

echo "-----> Enabling file sharing (afp), screen sharing (vnc) and remote login (ssh)"
sudo defaults write /var/db/launchd.db/com.apple.launchd/overrides.plist com.apple.screensharing -dict Disabled -bool false
start_service /System/Library/LaunchDaemons/com.apple.screensharing.plist
sudo defaults write /var/db/launchd.db/com.apple.launchd/overrides.plist com.apple.AppleFileServer -dict Disabled -bool false
start_service /System/Library/LaunchDaemons/com.apple.AppleFileServer.plist
silently ignore_error sudo systemsetup -setremotelogin on

##FINDER: SHOW ALL FILENAME EXTENSIONS
echo "-----> Show all filename extensions"
defaults write NSGlobalDomain AppleShowAllExtensions -bool true

##FINDER: ALLOW TEXT SELECTION IN QUICK LOOK
echo "-----> FINDER: ALLOW TEXT SELECTION IN QUICK LOOK"
defaults write com.apple.finder QLEnableTextSelection -bool true

echo "-----> DISABLE THE WARNING WHEN CHANGING A FILE EXTENSION"
defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false

echo "-----> AVOID CREATING .DS_STORE FILES ON NETWORK VOLUMES"
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true

##USE LIST VIEW IN ALL FINDER WINDOWS BY DEFAULT
##YOU CAN SET THE OTHER VIEW MODES BY USING ONE OF THESE FOUR-LETTER CODES: ICNV, CLMV, FLWV
defaults write com.apple.finder FXPreferredViewStyle -string “Nlsv”

echo "----->DISABLE THE WARNING BEFORE EMPTYING THE TRASH"
defaults write com.apple.finder WarnOnEmptyTrash -bool false

## REMOVE UN-NEEDED LINKS IN SAFARI
defaults write com.apple.Safari ProxiesInBookmarksBar "()"

echo "-----> TURN OFF SIDEBAR ON SAFARI TOPSITES"
defaults write com.apple.Safari ShowSidebarInTopSites -bool false

echo "-----> TURN OFF DASHBOARD"
defaults write com.apple.dashboard mcx-disabled -boolean YES

echo "-----> UNHIDE YOUR USER LIBRARY"
chflags nohidden ~/Library

echo "-----> TURN OFF ANIMATIONS"
defaults write com.apple.finder DisableAllAnimations -bool true

echo "-----> DISABLE SEND AND REPLY ANIMATIONS IN MAIL.APP"
defaults write com.apple.mail DisableReplyAnimations -bool true
defaults write com.apple.mail DisableSendAnimations -bool true
fi

########################
# DOC UTIL
# https://github.com/kcrawford/dockutil
########################

cd /Users/adamschoonover/Git/Personal/Post-install-scripts/OSX/dockutil/scripts

cp dockutil /usr/local/bin
chown root:wheel /usr/local/bin/dockutil
chmod 755 /usr/local/bin/dockutil

APP="/Applications"
CASKROOM="/opt/homebrew-cask/Caskroom"
dockutil --add $APP/Path@20Finder.app --position 1
dockutil --add $CASKROOM/google-chrome/latest/Google@20Chrome.app --after 'Safari'
docktuil --add $APP/Messages.app --position 6
docktuil --add $APP/iTerm.app --after 'Messages'
docktuil --add $APP/Quiver.app --after 'iTerm'
docktuil --add $CASKROOM/atom/1.5.4/Atom.app --after 'Quiver'
