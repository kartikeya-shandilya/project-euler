
for ($a=1;$a<=5000;$a++) {
        for ($b=$a+1;$b<=5000;$b++) {
                for ($c=$b+1;$c<=5000;$c++) {
                        if (sqrt($c+$b) eq int(sqrt($c+$b))) {
                        if (sqrt($c-$b) eq int(sqrt($c-$b))) {
                        if (sqrt($b+$a) eq int(sqrt($b+$a))) {
                        if (sqrt($b-$a) eq int(sqrt($b-$a))) {
                        if (sqrt($c+$a) eq int(sqrt($c+$a))) {
                        if (sqrt($c-$a) eq int(sqrt($c-$a))) {
			print $a," ",$b," ",$c,"\n";
			}}}}}}
		}
	}
}
