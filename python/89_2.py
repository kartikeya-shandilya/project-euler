
f=open("roman.txt")

rToA = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def romanToArabic(r):
    r=r.replace("IV","IIII")
    r=r.replace("IX","VIIII")
    r=r.replace("XL","XXXX")
    r=r.replace("XC","LXXXX")
    r=r.replace("CD","CCCC")
    r=r.replace("CM","DCCCC")
    return sum([rToA[c] for c in r])

def arabicToRoman(a):
    if   a/1000: return "M"*(a/1000) + arabicToRoman(a%1000)
    elif a>=900: return "CM" + arabicToRoman(a-900)
    elif a>=500: return "D"  + arabicToRoman(a-500)
    elif a>=400: return "CD" + arabicToRoman(a-400)
    elif a/100:  return "C"*(a/100)  + arabicToRoman(a%100)
    elif a>=90:  return "XC" + arabicToRoman(a-90)
    elif a>=50:  return "L"  + arabicToRoman(a-50)
    elif a>=40:  return "XL" + arabicToRoman(a-40)
    elif a>=10:  return "X"*(a/10)   + arabicToRoman(a%10)
    elif a==9:   return "IX"
    elif a>=5:   return "V"  + arabicToRoman(a-5)
    elif a==4:   return "IV"
    elif a>=1:   return "I"*a
    return ""

sav = 0
for line in f.readlines():
    a=romanToArabic(line.strip())
    r=arabicToRoman(a)
    sav += len(line.strip()) - len(r)

print sav
# sav: 743
