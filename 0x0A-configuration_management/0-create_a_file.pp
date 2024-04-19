#create a file
# Define a file resource to create the file in /tmp
file { '/tmp/school':
ensure => present,
content => "I love Puppet",
mode => '0744',
owner => 'www-data',
group => 'www-data',
}
