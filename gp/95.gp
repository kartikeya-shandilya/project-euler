sod(n) = sumdiv(n, i, i) - n
upp_lim = 1000000;
smart_sod = matrix(1, upp_lim);
for(i=1, upp_lim, smart_sod[1, i] = sod(i));

str_lim = 1; chk_lim = 1000000;
chk = matrix(1, upp_lim); chk[1, 1] = 1;
loop_str = str_lim; max_len = 0;

while(1,{
	test_ind = loop_str = loop_str+1;
	if(loop_str>chk_lim, break);
	loop_len = 0;
	if(chk[1, loop_str]!=0, next);
	\\if(test_ind%5000==0,print("test_ind:",test_ind,"..."));
	while(1,\
		if(test_ind>upp_lim || test_ind<loop_str, loop_len=0; break);
		if(chk[1, test_ind]!=0, if(chk[1, test_ind]\1000000!=loop_str, loop_len=0; break, loop_len-=chk[1, test_ind]%1000000; break));
		chk[1, test_ind] = loop_str*1000000 + loop_len;
		test_ind = smart_sod[1, test_ind];
		loop_len += 1;
	);
	if(loop_len>0, print("loop_str:",loop_str," loop_len:",loop_len));
	if(loop_len>max_len, max_len=loop_len);
});
