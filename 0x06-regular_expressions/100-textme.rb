#!/usr/bin/env ruby
from = ARGV[0].scan(/(?<=(?:from:))[\w+|\+?\d+]/)
from1 = ARGV[0].scan(/(?<=(?:from:))\+?\d+/)
to = ARGV[0].scan(/(?<=(?:to:))[(\w+|\+?\d+]/)
to1 = ARGV[0].scan(/(?<=(?:to:))\+?\d+/)
flags = ARGV[0].scan(/(?<=(?:flags:))-?\d+:-?\d+:-?\d+:-?\d+:-?\d+/)
puts "#{from[0]},#{to[0]},#{flags[0]}"
