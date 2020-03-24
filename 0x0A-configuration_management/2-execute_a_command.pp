# Using Puppet, kills a process named killmenow

exec { 'killnow':
  path    => ['/usr/bin', '/bin', '/sbin', '/usr/local/bin'],
  command => 'pkill killmenow',
}
