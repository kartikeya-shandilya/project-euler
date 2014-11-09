#$i=0;

for ($k=1;$k<=4;$k++) {
for ($j=$k+1;$j<=4;$j++) {
for ($m=1;$m<=4;$m++) {
for ($l=$m+1;$l<=4;$l++) {

	$a=$j**2-$k**2;
	$b=2*$j*$k;
	$c=$l**2-$m**2;
	$d=2*$l*$m;
	$X=($a**2+$b**2)*($c**2+$d**2);
	$Y=2*$a*$b*($c**2+$d**2);
	$Z=2*$c*$d*($a**2+$b**2);
	
	if ($Y > $Z) {
	print "\n";
	print "j=",$j," k=",$k," l=",$l," m=",$m,"\n";
	print "a=",$a," b=",$b," c=",$c," d=",$d,"\n";
	print "x=",$X," y=",$Y," z=",$Z,"\n";
	print "x+y=",$X+$Y," is ",sqrt($X+$Y)," squared \n";
	print "x-y=",$X-$Y," is ",sqrt($X-$Y)," squared \n";
	print "x+z=",$X+$Z," is ",sqrt($X+$Z)," squared \n";
	print "x-z=",$X-$Z," is ",sqrt($X-$Z)," squared \n";
	print "x+y+z=",$X+$Y+$Z,"\n\n";
	}
	
#	if ($Y > $Z) {
#	if (sqrt($Y+$Z) eq int(sqrt($Y+$Z))) {
#		$i++;
#		if (($i % 50) eq 0) { print ".."; }
#	if (sqrt($Y-$Z) eq int(sqrt($Y-$Z))) {
#		print "\n";
#		print "j=",$j," k=",$k," l=",$l," m=",$m,"\n";
#		print "a=",$a," b=",$b," c=",$c," d=",$d,"\n";
#		print "x=",$X," y=",$Y," z=",$Z,"\n";
#		print "x+y+z=",$X+$Y+$Z,"\n\n";
#		break;
#	}}}
}}}}
