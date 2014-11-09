#!/usr/bin/perl

for ($x=1,$max=0;$x<500;$x++) {
	$count=0;
	for ($l=1;$l<=int(sqrt($x/6));$l++) {
		if ($x % $l eq 0) {
			for ($m=int(sqrt($x/(4*$l)));$m<=int(sqrt($x/(2*$l)));$m++) {
				if (($x/$l)%$m eq 0) {
					$count++;
				}
			}
		}
	}
	if ($count>$max) {
		$max=$count;
		$ans=$x;
		print "$x has $count count\n";
	}
}
