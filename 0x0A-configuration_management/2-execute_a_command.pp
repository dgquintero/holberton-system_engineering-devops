# Using Puppet, kills a process named killmenow

exec { 'killnow':
  command   => 'pkill killmenow',
  provider  => 'shell',
}
