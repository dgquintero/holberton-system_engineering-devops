# Apache has 500 error
exec { 'fix_error_500':
  command => "sed -i s/phpp/php /vas/www/html/wp-settings.php",
  path    => '/bin/',
}
