echo "Welcome to Grove Indoor Environment Kit Intelligent System"

git clone https://github.com/xe1gyq/GiekIs.git
cd GiekIs/
pip install pip --upgrade
sh requirements.opkg
pip install -r requirements.pip
git clone https://github.com/xe1gyq/core.git
git checkout -b basic origin/basic

echo
echo "Now go to GiekIs directory to get started!"
echo
echo "Work on having your credentials ready as described under"
echo "https://xe1gyq.gitbooks.io/core/content/documentation/Credentials.html"
echo
echo "The following files need to be modified"
echo
echo "core/configuration/credentials.config"
echo "core/configuration/voicerss.ak"
echo "core/configuration/voicerss.mk"
echo
echo "Happy GiekIs'ing"
