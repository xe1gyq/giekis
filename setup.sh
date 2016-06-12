echo "Welcome to Grove Indoor Environment Kit Intelligent System"

git clone https://github.com/xe1gyq/giekis.git
cd giekis/
pip install -r requirements.pip
sh requirements.opkg
git clone https://github.com/xe1gyq/core.git

echo "Now go to giekis directory to get started!"
echo "First work on having your credentials ready as described under"
echo "https://xe1gyq.gitbooks.io/core/content/documentation/Credentials.html"
echo "under giekis/core/configuration/credentials.config"

echo "Happy giekis'ing"
