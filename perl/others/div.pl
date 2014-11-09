#!/usr/bin/perl

use Math::BigInt;

my $a = Math::BigInt->new('11235234623534535212421343457');
my $b = Math::BigInt->new('2');

while ($a > 1)
{
  $c=$a-(($a/$b)*2);
  if ($c>2) {
	$r=$c%2;
	$a=($a/$b)+($c/2);
  }
  else { $a=$a/$b; }
  print "$a $c\n";
}
