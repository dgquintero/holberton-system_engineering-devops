# Using Puppet, kills a process named killmenow

exec { 'killnow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
