#!/usr/bin/perl
$range=shift;
use Math::Complex;

$Prime[0]=2;
$Prime[1]=3;
$Prime[2]=5;

for ($n=7;$n<$range;) {
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

for ($i=0,$sum=0;$Prime[$i] ne "";$i++) {
	$sum=$sum+$Prime[$i];
}

print $sum,"\n";
