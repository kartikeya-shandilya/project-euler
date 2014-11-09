#!/usr/bin/perl

for ($a=0;$a<=9;$a++) {
for ($b=0;$b<=9;$b++) {
for ($c=0;$c<=9;$c++) {
for ($d=0;$d<=9;$d++) {
for ($e=0;$e<=9;$e++) {
for ($f=0;$f<=9;$f++) {
for ($g=0;$g<=9;$g++) {
for ($h=0;$h<=9;$h++) {
for ($i=0;$i<=9;$i++) {
 $c1=12-($a+$b+$c);
 $c2=12-($d+$e+$f);
 $c3=12-($g+$h+$i);
 $c4=12-($a+$d+$g);
 $c5=12-($b+$e+$h);
 $c6=12-($c+$f+$i);
 $c7=12-($a+$e+$i);
 $di=$c1+$f+$h+$c4;
 $s1=$c1+$c2+$c3+$c7;
 $s2=$c4+$c5+$c6+$c7;
 if(($c1>=0 and $c2>=0 and $c3>=0 and $c4>=0 and $c5>=0 and $c6>=0 and $c7>=0)and 
    (9>=$c1 and 9>=$c2 and 9>=$c3 and 9>=$c4 and 9>=$c5 and 9>=$c6 and 9>=$c7)and
    ($di eq 12)and($s1 eq 12)and($s2 eq 12)) {
	print "$a $d $g $c4\n$b $e $h $c5\n$c $f $i $c6\n$c1 $c2 $c3 $c7\n--------\n";
	$count ++;
 }
}}}}}}}}}

print $count,"\n";
