#this script installs what you'll need for the database

sudo apt-get update -y
sudo apt-get upgrade -y
#sudo apt-get install postgresql postgresql-contrib -y
sudo apt install mysql-server -y
sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
sudo apt-get install python3-pip -y
python -m pip install mysql-connector-python
echo "Prerequsites installed, my guy!"