#this script installs what you'll need for the database

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install postgresql postgresql-contrib -y
sudo apt-get install python3-pip -y
pip3 install psycopg2-binary

echo "Prerequsites installed!"