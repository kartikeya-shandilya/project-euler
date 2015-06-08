#!/usr/bin/perl
use Math::Complex;

$Prime[0]=2;
$Prime[1]=3;
$Prime[2]=5;

for ($n=7;$n<110000;) {
	$d=0;
	for ($i=0;$Prime[$i]<sqrt($n)+1;$i++) {
		if($Prime[$i] ne 0) {
			if($n%$Prime[$i] eq 0){
				$d=1;
			}
		}
	}
	if ($d eq 0) {
		$Prime[$#Prime+1]=$n;
	}
	$n=$n+2;
}

print $Prime[10000],"\n";
