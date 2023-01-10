# Using Puppet to create  a file in /tmp

$doc_root = '/tmp/'

file { "${doc_root}/school":
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
