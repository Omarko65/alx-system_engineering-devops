# a puppet script that creates a file in tmp

file { '/tmp/school':
  ensure  => 'present',
  replace => 'no',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
