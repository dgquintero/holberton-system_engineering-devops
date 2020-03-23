exec { 'killnow':
  command   => 'pkill killmenow',
  provider  => 'shell',
}
