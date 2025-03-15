sudo yum list | grep python3
python3 --version
sudo yum install -y python3-pip python3 python3-setuptools
echo "===>PIP install boto3"
pip3 install boto3
echo "===> PIP install mysql_connector_python"
pip3 install mysql_connector_python
mkdir ~/user_files
echo "User files directory has been created."
echo "Scheduling cron job for every 5 minutes"
*/5 * * * * ~/file_move.sh

