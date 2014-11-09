#!/usr/bin/perl
use Math::BigInt;

$start=shift;
#$a = Math::BigInt->new('298023223876953125');
$a = Math::BigInt->new('1');
$a=$start;

$ans=ways($a);
print "f(",$a,") = ",$ans,"\n";

sub binary {
	my $a=shift;
	my $b=Math::BigInt->new('1');
	my $c=Math::BigInt->new('0');
	while ($a>0) {
		$c=$c+$b*($a%2);
		$b=10*$b;
		$a=Math::BigInt->new(int($a/2));
#		print "$a $b $c\n";
	}
	return ($c);
}

sub ispower {
	my $x=shift;
	my @y=split//,$x;
#	print "binary\n",$x," ",$#y,"\n";
	my $i,$j;
	for ($i=0,$j=0;$i<=$#y;$i++) {
		$j=$j+$y[$i];
	}
	if ($j eq $#y+1) { return (1); }
	elsif ($j eq 1) { return ($#y+1); }
	elsif (($j eq 2)and($y[$#y] eq 1)) { return ($#y); }
	else { return (0); }
}

sub ways {
	my $x=shift;
	my $y=binary($x);
	my $z=ispower($y);
#	print "ways\n",$x," ",$y," ",$z,"\n";
	if ($z ne 0) { 
#		print "f(",$x,") = ",$z,"\n";  
		return ($z); 
	}
	else { 
		if($x%2 eq 1) { 
#			print "f(",$x,") = f(",($x-1)/2,")\n"; 
			$ans=ways(($x-1)/2); return($ans); 
		}
		else {
#			print "f(",$x,") = f(",$x/2,") + f(",($x-2)/2,")\n";
			$ans=ways($x/2)+ways(($x-2)/2);
			return($ans); 
		}
	}
}

