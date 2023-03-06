# A puppet manifessts that fixes a lamp wordpress webstack
exec { 'fix-wordpress':
  command => "/bin/sed -i 's/phpp/php/' /var/www/html/wp-settings.php"
}
