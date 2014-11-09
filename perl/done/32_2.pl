#!/usr/bin/perl

$result=0;

for ($n=1; $n<10; $n++) {
	$ans=$ans+1/$n;
}
for ($i=1;$i<50;$i++) {
	for ($j=130;$j<2000;$j++) {
		$k=$i*$j;
		$sum=0;
		$pro=1;
		$rec=0;
		for ($x=$i; $x>0; $x=int($x/10)) {
			$sum=$sum+$x%10;
			if($x%10 ne 0) {$pro=$pro*($x%10);}
			if($x%10 ne 0) {$rec=$rec+1/($x%10);}
			else {$sum=0.01; $pro=0.01; $rec=0.01}
		}
		for ($x=$j; $x>0; $x=int($x/10)) {
			$sum=$sum+$x%10;
			if($x%10 ne 0) {$pro=$pro*($x%10);}
			if($x%10 ne 0) {$rec=$rec+1/($x%10);}
			else {$sum=0.01; $pro=0.01; $rec=0.01}
		}
		for ($x=$k; $x>0; $x=int($x/10)) {
			$sum=$sum+$x%10;
			if($x%10 ne 0) {$pro=$pro*($x%10);}
			if($x%10 ne 0) {$rec=$rec+1/($x%10);}
			else {$sum=0.01; $pro=0.01; $rec=0.01}
		}
		if (($sum eq 45) and ($pro eq 362880) and ($rec eq $ans))
		{
			print $i," x ",$j," = ",$k,"\n";
			$result=$result+$k;
		}
	}
}

print "\n$result\n";


#	27 x 594 = 16038
#	36 x 495 = 17820
#	39 x 402 = 15678
#	45 x 396 = 17820
#	46 x 715 = 32890
#	52 x 367 = 19084
#	54 x 297 = 16038
#	78 x 345 = 26910
#	63 x 927 = 58401


#	3 x 5694 = 17082
#	4 x 3907 = 15628
#	4 x 7039 = 28156
#	4 x 9127 = 36508
#	6 x 5817 = 34902
#	
#	3 x 6819 = 20457
#	3 x 6918 = 20754
#	3 x 8169 = 24507
#	3 x 9168 = 27504
#	
#	7 x 3094 = 21658
#	7 x 4093 = 28651
#	7 x 9304 = 65128
#	7 x 9403 = 65821

