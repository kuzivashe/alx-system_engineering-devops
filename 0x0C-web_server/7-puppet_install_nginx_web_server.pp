# commands in puppet in order to configure our Nginx

exec {'install':
  command  => 'sudo apt update ; sudo apt -y install nginx ; echo "Hello World" | sudo tee /var/www/html/index.html',
  provider => shell,
}
exec {'default':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com/channel/UC-QtMoPv-9g1vD7PoyKQtEw permanent;/" /etc/nginx/sites-available/default ; sudo service nginx restart',
  provider => shell,
}
