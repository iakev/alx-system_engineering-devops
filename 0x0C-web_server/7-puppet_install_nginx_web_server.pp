# puppet file to installl and configure an Nginx web server

$doc_root  = '/var/www'
$conf_root = '/etc/nginx/sites-available'

#install Nginx on server
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

exec { 'apt-get update':
  command => '/usr/bin/apt-get -y update'
}

##configure Nginx

file {$doc_root:
  ensure => 'directory'
}

# add a root directories
file {"${doc_root}/example.com":
  ensure  => 'directory',
  require => File[$doc_root]
}
file {"${doc_root}/example.com/text":
  ensure  => 'directory',
  require => File["${doc_root}/example.com"]
}

file {"${doc_root}/example.com/text/hello":
  ensure  => 'present',
  content => "Hello World!\n",
  require => File["${doc_root}/example.com/text"]
}

# add a custome error page

file {"${doc_root}/example.com/text/error":
  ensure  => 'present',
  content => "Ceci n\'est pas une page\n",
  require => File["${doc_root}/example.com/text"]
}

# configure site configuration using virtual hosts (server blocks)

file {$conf_root:
  ensure  => 'directory',
  require => Package['nginx']
}

file {"${conf_root}/example.com":
  ensure        => 'present',
  content       => "# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
server {
       listen 80;
       listen [::]:80;

       server_name  example.com;

       root /var/www/example.com/text;
       index hello;

       # Everything is a 404
       location / {
       		try_files \$uri \$uri/ =404;
       }

       location /redirect_me {
       		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /error;
	location = /error {
		 root /var/www/example.com/text;
		 internal;
	}
}",
        require => File[$conf_root],
        notify  => Service['nginx']
}

# enable example.com conf by addying symlink to sites-enabled
exec {'activate example.com':
  command => '/usr/bin/ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/',
}

# remove default file from sites-anabled
exec {'remove default':
  command => '/usr/bin/rm /etc/nginx/sites-enabled/default',
  onlyif  => '/usr/bin/ls /etc/nginx/sites-enabled/default',
  require => Package['nginx']
}

#restart nginx to have the changes commited
service { 'nginx':
  ensure => running,
  enable => true
}
