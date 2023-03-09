# Puppet manifest to fix and increase open files for nginx
$str = '# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 10000"
'

file {'/etc/default/nginx':
  notify  => Service['nginx'],
  content => $str
}

service {'nginx':
  ensure => 'running',
  enable => true
}
