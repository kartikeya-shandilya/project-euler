
clean:
	paste -s -d',,,,,,\n' todo/proe_solved.txt | cut -f1 > todo/proe_solved_clean.txt

gt_done_code:
	cat todo/proe_files.txt todo/proe_solved_clean.txt | sort -n | uniq -d > todo/proe_done_code.txt	
gt_done_nocode:
	cat todo/proe_files.txt todo/proe_solved_clean.txt | sort -n | uniq -u > todo/proe_uniq.txt;\
	cat todo/proe_uniq.txt todo/proe_solved_clean.txt | sort -n | uniq -d > todo/proe_done_nocode.txt
gt_notdone:
	cat todo/proe_uniq.txt todo/proe_files.txt | sort -n | uniq -d > todo/proe_notdone.txt
gt_all: gt_done_code gt_done_nocode gt_notdone
