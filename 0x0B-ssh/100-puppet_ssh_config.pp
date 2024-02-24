# make changes to config file using puppet

$content = 'Host 349756-web-01
	HostName 34.204.95.98
	User ubuntu
	IdentityFile ~/.ssh/school
	PasswordAuthentication no'

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => $content,
}
