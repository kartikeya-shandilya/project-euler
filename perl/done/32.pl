#!/usr/bin/perl

for ($i=0;$i<10;$i++) {
	$A[$i]=1;
	for ($j=$i;$j>0;$j--) {
		$A[$i]*=$j;
	}
}

for ($i=3;$i<10000000;$i++) {
	@B=split//,$i;
	for ($k=0,$j=0;$k<=$#B;$k++) {
		$j=$j+$A[$B[$k]];
	}
	if($i eq $j) {
		print $i,"\n";
		$sum=$sum+$i;
	}
}

print $sum,"\n";
