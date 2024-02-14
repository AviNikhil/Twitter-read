sudo apt-get update
sudo apt-get install openjdk-8-jdk -y
sudo apt-get install nodejs npm -y
cd /home/sainikhil/wallet_back/w_backend/
./mvnw clean package
mvn clean install
cd /home/sainikhil/wallet_front/w_frontend/
npm install
npm install axios
npm install react-router-dom
npm start
java -jar /home/sainikhil/wallet_back/w_backend/target/CapstoneProject-0.0.1-SNAPSHOT.jar &
echo "applica is running"

