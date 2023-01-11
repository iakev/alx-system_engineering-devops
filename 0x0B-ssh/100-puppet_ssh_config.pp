# A puppet manifest that configures a SSH client configuration file

file { 'sshclientconfig':
  ensure  => 'present',
  path    => 'etc/.ssh/ssh_config',
  content => 'Host *
                   PasswordAuthentication no
                   IdentityFile ~/.ssh/school'
}
