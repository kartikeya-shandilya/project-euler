#!/usr/bin/perl

for ($i=1;$i<500;$i++) {
	for ($j=1;$j<500;$j++) {
		$k=1000-($i+$j);
		$p=($i*$i)+($j*$j);
		$q=$k*$k;
		if ($p eq $q)
		{
			print $i," ",$j," ",$k,"\n";
			print $i*$j*$k;
		}
	}
}
