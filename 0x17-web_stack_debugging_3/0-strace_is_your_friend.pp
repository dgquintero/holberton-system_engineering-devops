exec { 'fix_error_500':
  onlyif  => 'test -e /var/www/html.php',
  command => "sed -i s/phpp/php /vas/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
