m=max(power)
if(armor<=m):
    return sum(power)-armor+1
else:
    return sum(power)-m+1