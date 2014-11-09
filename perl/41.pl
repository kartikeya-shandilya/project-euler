#!/usr/bin/perl

use Math::Combinatorics;

my @n = qw(1 2 3 4);

print "permutations of 3 from: ".join(" ",@n)."\n";
print "------------------------".("--" x scalar(@n))."\n";
print join("\n", map { join " ", @$_ } permute(@n)),"\n";

