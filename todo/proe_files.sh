ls -lR * | awk '{print $9}' | cut -d. -f1 | sed "/^\s*$/d" | cut -d_ -f1 | sort -n | uniq -c | awk '{print $2}' | grep "^[1-9]" > proe_files.txt
#unix2dos.exe proe_files.txt
