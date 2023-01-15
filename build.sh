#!/usr/bin/env bash

mkdir -p ~/.tmp

if [ -d ~/.tmp/yay ]; then
    rm -rf ~/.tmp/yay
fi

git clone https://aur.archlinux.org/yay ~/.tmp/yay
cd ~/.tmp/yay &&
makepkg -sri

if [ -d ~/.miniconda ]; then
    rm -rf ~/.miniconda
fi

wget https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh -P ~/.tmp
bash ~/.tmp/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh -b -p ~/.miniconda

yay -S --needed --noconfirm --useask \
base \
base-devel \
ipe \
xmind \
lib32-mesa \
whatsie \
onlyoffice-bin \
prospect-mail-bin \
onedrive-abraunegg \
onedrivegui-git \
geany \
geany-plugins \
xmind \
nnn \
aria2-fast \
powerpill \
texlive-most \
texlive-lang \
texlive-bibtexextra \
texlive-fontsextra \
biber \
texstudio \
tllocalmgr \
visual-studio-code-bin \
vscodium-bin-marketplace \
jdk-openjdk \
direnv \
paccache-hook \
inkscape \
cmake \
git \
extra-cmake-modules \
plasma-wayland-session \
alsa-utils \
alsa-plugins \
alsa-firmware \
xf86-video-intel \
mesa \
python-virtualenv \
python-cssselect \
tk \
neofetch \
lolcat \
zip \
unzip \
unrar \
p7zip \
zsh \
npm \
nodejs-lts-gallium \
go \
ruby \
python-gobject \
cairo \
qt5-base \
qt6-base \
vulkan-intel \
wget \
curl \
snarf \
axel \
lftp \
chromium \
kitty \
qalculate-gtk \
pacutils \
pacman-contrib

if [ -d ~/.oh-my-zsh ]; then
    rm -rf ~/.oh-my-zsh
fi

mkdir -p tmp
if [ -d tmp/stupidsimplelauncher ]; then
    rm -rf tmp/stupidsimplelauncher
fi
git clone https://github.com/heqro/stupid-simple-launcher tmp/stupidsimplelauncher
if [ -d ~/.local/share/plasma/plasmoids/stupidsimplelauncher ]; then
    rm -rf ~/.local/share/plasma/plasmoids/stupidsimplelauncher
fi
cp -r tmp/stupidsimplelauncher/v1 ~/.local/share/plasma/plasmoids/stupidsimplelauncher
echo "Install StupidsimpleLauncher finished..."
if [ -d tmp/plasma-simpleMonitor ]; then
    rm -rf tmp/plasma-simpleMonitor
fi
git clone https://github.com/dhabyx/plasma-simpleMonitor.git tmp/plasma-simpleMonitor
if [ -d ~/.local/share/plasma/plasmoids/org.kde.simpleMonitor ]; then
    rm -rf ~/.local/share/plasma/plasmoids/org.kde.simpleMonitor
fi
cd tmp/plasma-simpleMonitor && 
plasmapkg2 -t plasmoid -i ./plasmoid
echo "Install plasma-simpleMonitor finished..."
if [ -d tmp/Burn-My-Windows ]; then
    rm -rf tmp/Burn-My-Windows
fi
git clone https://github.com/Schneegans/Burn-My-Windows tmp/Burn-My-Windows
if [ -d ~/.local/share/plasma/kwin/effects ]; then
    rm -rf ~/.local/share/kwin/effects/*
else
    mkdir -p ~/.local/share/plasma/kwin/effects
fi
bash tmp/Burn-My-Windows/kwin/build.sh
tar -xf tmp/Burn-My-Windows/kwin/burn_my_windows_kwin4.tar.gz -C ~/.local/share/kwin/effects
echo "Install Burn-My-Windows finished..."
if [ -d tmp/paneltransparencybutton ]; then
    rm -rf tmp/paneltransparencybutton
fi
git clone https://github.com/psifidotos/paneltransparencybutton tmp/paneltransparencybutton
if [ -d ~/.local/share/plasma/plasmoids/org.kde.paneltransparencybutton ]; then
    rm -rf ~/.local/share/plasma/plasmoids/org.kde.paneltransparencybutton
fi
cd tmp/paneltransparencybutton && plasmapkg2 -i .
cd ../..
echo "Install paneltransparencybutton finished..."
if [ -d tmp/PurpleBitch-Sddm ]; then
    rm -rf tmp/PurpleBitch-Sddm
fi
git clone https://github.com/sl33pz/PurpleBitch-Sddm tmp/PurpleBitch-Sddm
if [ -d ~/.local/share/sddm/themes/PurpleBitch ]; then
    rm -rf ~/.local/share/sddm/themes/PurpleBitch
else
    mkdir -p ~/.local/share/sddm/themes
fi
cp -r tmp/PurpleBitch-Sddm ~/.local/share/sddm/themes/PurpleBitch
echo "Install PurpleBitch-Sddm finished..."
if [ -d tmp/PurpleBitch-Icons ]; then
    rm -rf tmp/PurpleBitch-Icons
fi
git clone https://github.com/sl33pz/PurpleBitch-Icons tmp/PurpleBitch-Icons
if [ -d ~/.local/share/icons/PurpleBitch ]; then
    rm -rf ~/.local/share/icons/PurpleBitch
else
    mkdir -p ~/.local/share/icons
fi
cp -r tmp/PurpleBitch-Icons ~/.local/share/icons/PurpleBitch
echo "Install PurpleBitch-Icons finished..."
if [ -d tmp/PurpleBitch-Plasma ]; then
    rm -rf tmp/PurpleBitch-Plasma
fi
git clone https://github.com/sl33pz/PurpleBitch-Plasma tmp/PurpleBitch-Plasma
if [ -d ~/.local/share/plasma/desktoptheme ]; then
    rm -rf ~/.local/share/plasma/desktoptheme/PurpleBitch
else
    mkdir -p ~/.local/share/plasma/desktoptheme
fi
cp -r tmp/PurpleBitch-Plasma ~/.local/share/plasma/desktoptheme/PurpleBitch
echo "Install PurpleBitch-Plasma finished..."

rm -rf tmp


yes | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"