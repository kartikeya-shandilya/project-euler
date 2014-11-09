#!/usr/bin/perl

for ($i=900;$i<1000;$i++) {
	for ($j=900;$j<1000;$j++) {
		$k=$i*$j;
		$l=reverse $k;
		if ($l eq $k) {
			print $i,"*",$j,"=",$k,"\n";
		}
	}
}