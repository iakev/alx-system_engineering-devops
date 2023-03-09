#puppet manifest to increase file limits for holberton user
exec {'change-os-config-for-holberton-user':
  onlyif  => '/usr/bin/test -e /etc/security/limits.conf',
  command => "/bin/sed -i 's/nofile *[0-9]/nofile 1000000/g' /etc/security/limits.conf"
}
