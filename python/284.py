
alphanum={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",
	  16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"o",25:"p",26:"q",27:"r",28:"s",29:"t",
	  30:"u", 31:"v",32:"w",33:"x",34:"y",35:"z"}

alphanum2={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,
          "g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29,
          "u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

#def find_key(dic, val):
#    return [k for k, v in dic.iteritems() if v == val][0]

def toBase(x, base=14):
    s=""
    while(1):
        y=x%base
        x=x/base
        s=alphanum[y]+s
        if not x:
            break
        elif(x<base):
            s=alphanum[x]+s
            break
    return s

def toDecimal(x, base=14):
    z=len(x)
    y=0
    for char in x:
        z=z-1
        y=y+base**z*alphanum2[char]
    return y

def getNext(i,lst=[""],sqs=[0],sod=[0],pow1=1,pow2=1,base=14):
    newList=[]
    newsqrs=[]
    newsods=[]
    if i==0:
        pow1=1
        pow2=1
    else:
        pow1=pow1*base
        pow2=pow2*base**2
    for n in xrange(len(lst)):
        elm=lst[n]
        num=sqs[n][0]
        sqr=sqs[n][1] 
        sum=sod[n]
        for i in xrange(base):
            x=alphanum[i]+elm
            #print x,
            #print toDecimal(x)**2, num,
            tmp=i**2*pow2+i*pow1*(num<<1)+sqr
            y=toBase(tmp, base)
            #print tmp, y
            if y[-len(x):]==x:
                newList.append(x)
                newsqrs.append([i*pow1+num,tmp])
                newsods.append(i+sum)
    return newList,newsqrs,newsods,pow1,pow2

#"""
base=14
upto=1000
ans=[""]
sod=[0]
sqs=[[0,0]]
pow1=1
pow2=1
sum=0
for i in xrange(upto):
    ans,sqs,sod,pow1,pow2=getNext(i,ans,sqs,sod,pow1,pow2,base)
#    print "%s:%s"%(i,len(ans))
#    print "ans:::::", ans
#    for elm in ans:
#        print "elm=>", elm
#        if elm[0]!="0":
#            for char in elm:
#                sum=sum+alphanum2[char]
#            print "sum->", sum
    for i in xrange(len(ans)):
        trm=sod[i]
        sum=sum+trm*(ans[i][0]!='0')

print "\n",toBase(sum)

#"""
