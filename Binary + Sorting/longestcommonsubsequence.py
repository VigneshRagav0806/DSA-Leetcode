def longestcommonsubsequence(text1,text2,n,m):
    if m==0 or n==0:
        return 0

    if text1[n-1]==text2[m-1]:
        return 1+longestcommonsubsequence(text1,text2,n-1,m-1)
    else:
        return max(longestcommonsubsequence(text1,text2,n-1,m), longestcommonsubsequence(text1,text2,n,m-1))


string1="dfggfhdghfdbgnghzgb"
string2="ghdggzb"
n=len(string1)
m=len(string2)
lcs=longestcommonsubsequence(string1,string2,n,m)
print(lcs)
