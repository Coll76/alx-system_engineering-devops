#!/usr/bin/env ruby
#regular expression must match School
#Ruby script that accepts one argument and pass it to a regular expression matching method
puts ARGV[0].scan(/School/).join
