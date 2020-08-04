# Create a manifest that kills killmenow process
exec { 'killmenow':
    command => '/usr/bin/pkill killmenow'
}
