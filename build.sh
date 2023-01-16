#!/usr/bin/env bash




directories=("tmp"
            "$HOME/.miniconda"
            "$HOME/.oh-my-zsh"
            "$HOME/.local/share/plasma/plasmoids/org.kde.paneltransparencybutton"
            "$HOME/.local/share/plasma/plasmoids/org.kde.simpleMonitor"
            "$HOME/.local/share/plasma/plasmoids/stupidsimplelauncher"
            "$HOME/.local/share/kwin/effects"
            "$HOME/.local/share/plasma/plasmoids/com.github.prayag2.aestheticclock"
            "$HOME/.local/share/plasma/plasmoids/P-Connor.PlasmaDrawer")

mkdir -p tmp

sudo pacman-mirrors -c Germany -m rank
sudo pacman -S -q --noconfirm --needed base base-devel go


for d in "${directories[@]}"; do
    [ -d "$d" ] && rm -rf "$d" && sleep 1.5
done

git clone https://aur.archlinux.org/yay tmp/yay &>/dev/null
cd tmp/yay && makepkg -sri --noconfirm &>/dev/null && cd - &&
echo "Erfolgreich installiert: Yay"

mkdir -p "$HOME"/.local/share/kwin/effects


yay -S -q --noconfirm --needed \
alsa-utils \
alsa-firmware \
alsa-plugins \
sof-firmware \
xf86-video-intel \
vulkan-intel \
lib32-mesa \
mesa \
intel-ucode \
ipe \
xmind \
onlyoffice-bin \
whatsie \
visual-studio-code-bin \
vscodium-bin-marketplace \
texstudio \
texlive-most \
texlive-lang \
texlive-bibtexextra \
texlive-fontsextra \
biber \
zsh \
tllocalmgr \
python-virtualenv \
python-cssselect \
python-numpy \
tk \
python-gobject \
cairo \
bash-completion \
zsh-completions \
onedrive-abraunegg \
onedrivegui-git \
neofetch \
lolcat \
chromium \
kitty \
inkscape \
gwenview \
curl \
snarf \
axel \
lftp \
aria2-fast \
pacman-contrib \
pacutils \
paccache-hook \
qalculate-gtk \
klassy-git \
lightly-git \
ruby \
npm \
nodejs-lts-gallium \
jre-openjdk \
qt5-base \
qt6-base \
geogebra \
micro \
ttf-fira-code

wget https://github.com/Schneegans/Burn-My-Windows/releases/latest/download/burn_my_windows_kwin4.tar.gz -P tmp &>/dev/null
tar -xf tmp/burn_my_windows_kwin4.tar.gz -C "$HOME"/.local/share/kwin/effects
echo "Erfolgreich installiert: Burn My Windows"

git clone https://github.com/prayag2/kde_aestheticclock tmp/kde_aestheticclock &>/dev/null
cd tmp/kde_aestheticclock && kpackagetool5 -i package &>/dev/null && cd - &&
echo "Erfolgreich installiert: Aesthetic Clock"

git clone https://github.com/psifidotos/paneltransparencybutton tmp/paneltransparencybutton &>/dev/null
cd tmp/paneltransparencybutton && plasmapkg2 -i . &>/dev/null && cd - &>/dev/null &&
echo "Erfolgreich installiert: Transparency Panel Button"

git clone https://github.com/P-Connor/plasma-drawer tmp/plasma-drawer &>/dev/null
cd tmp && plasmapkg2 -i plasma-drawer/ &>/dev/null && cd - &>/dev/null &&
echo "Erfolgreich installiert: Plasma Drawer"

git clone https://github.com/dhabyx/plasma-simpleMonitor.git tmp/plasma-simpleMonitor &>/dev/null
cd tmp/plasma-simpleMonitor/ && plasmapkg2 -t plasmoid -i ./plasmoid &>/dev/null && cd - &>/dev/null &&
echo "Erfolgreich installiert: Plasma SimpleMonitor"

git clone https://github.com/dfaust/plasma-applet-netspeed-widget tmp/plasma-applet-netspeed-widget &>/dev/null
cd tmp/plasma-applet-netspeed-widget && mkdir build && cd build &&
cmake -DCMAKE_INSTALL_PREFIX=/usr .. &>/dev/null
wait
make &>/dev/null
wait
sudo make install &>/dev/null && cd ../../.. &&
wait

echo "Erfolgreich installiert: NetspeedWidget"

if [ -d /usr/share/plasma/desktoptheme/PurpleBitch ]; then
    sudo rm -rf /usr/share/plasma/desktoptheme/PurpleBitch
fi
if [ -d /usr/share/icons/PurpleBitch ]; then
    sudo rm -rf /usr/share/icons/PurpleBitch
fi
if [ -d /usr/share/sddm/themes/PurpleBitch ]; then
    sudo rm -rf /usr/share/sddm/themes/PurpleBitch
fi

git clone https://github.com/sl33pz/PurpleBitch-Plasma tmp/PurpleBitch-Plasma &>/dev/null
sudo mv tmp/PurpleBitch-Plasma /usr/share/plasma/desktoptheme/PurpleBitch
echo "Erfolgreich installiert: PurpleBitch Plasma"

git clone https://github.com/sl33pz/PurpleBitch-Icons tmp/PurpleBitch-Icons &>/dev/null
sudo mv tmp/PurpleBitch-Icons /usr/share/icons/PurpleBitch
echo "Erfolgreich installiert: PurpleBitch Icons"

git clone https://github.com/sl33pz/PurpleBitch-Sddm tmp/PurpleBitch-Sddm &>/dev/null
sudo mv tmp/PurpleBitch-Sddm /usr/share/sddm/themes/PurpleBitch
echo "Erfolgreich installiert: PurpleBitch SDDM"

rm -rf tmp

yes | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

sed -i 's/zsh/ /m' "$HOME/.bashrc"
echo "zsh" >> "$HOME"/.bashrc




git clone https://github.com/zsh-users/zsh-autosuggestions "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-syntax-highlighting



