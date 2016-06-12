echo "Welcome to Grove Indoor Environment Kit Intelligent System"

git clone https://github.com/xe1gyq/GiekIs.git
cd GiekIs/
pip install -r requirements.pip
sh requirements.opkg
git clone https://github.com/xe1gyq/core.git

echo
echo "Now go to GiekIs directory to get started!"
echo
echo "First work on having your credentials ready as described under"
echo "https://xe1gyq.gitbooks.io/core/content/documentation/Credentials.html"
echo "under GiekIs/core/configuration/"
echo
echo "The following files need to be present"
echo "credentials.config  voicerss.ak voicerss.mk"
echo
echo "Happy GiekIs'ing"
