# Create package flask from provider pip3
# Version must be 2.1.0

package {'Flask':
ensure => '2.1.0',
provider => 'pip3',
}
