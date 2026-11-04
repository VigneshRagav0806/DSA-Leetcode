def lengthoflastword(s) -> int:
    start=len(s)-1
    while start>=0 and s[start]==' ':
        start-=1
    end=start
    while end>=0 and s[end]!=' ':
        end-=1
    return start-end

length=lengthoflastword("Hello World")
print(length)