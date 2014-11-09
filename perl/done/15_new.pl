#!/usr/bin/perl

for ($i=0;$i<4;$i++) {
	$Mat[0][$i]=$i+2;
	$Mat[$i][0]=$i+2;
}

for ($i=1;$i<4;$i++) {
	for ($j=1;$j<4;$j++) {
		$Mat[$i][$j]=$Mat[$i-1][$j]+$Mat[$i][$j-1];
	}
}

$ans=$Mat[0][0];
print "No of paths are: ",$ans,"\n";

