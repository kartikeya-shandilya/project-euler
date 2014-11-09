#!/usr/bin/perl

$ans=routes(10,10);

print "No of paths are: ",$ans,"\n";

sub routes {
	my $x=shift;
	my $y=shift;
	my $a;
	my $b;
	my $c;
	if (($x eq 1) and ($y eq 1)) {
		return (2);
	}
	if (($x eq 1) and ($y ne 1)) {
		$a=routes(1,$y-1);
		$b=$a+1;
		return ($b);
	}
	if (($x ne 1) and ($y eq 1)) {
		$a=routes($x-1,1);
		$b=$a+1;
                return ($b);
	}
	if (($x ne 1) and ($y ne 1)) {
		$a=routes($x,$y-1);
		$b=routes($x-1,$y);
		$c=$a+$b;
                return ($c);
	}
}
