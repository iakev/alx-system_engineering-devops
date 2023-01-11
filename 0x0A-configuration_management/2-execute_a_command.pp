# A manifest that executes a command

exec {'killproc':
  command => '/usr/bin/pkill killmenow',
}
