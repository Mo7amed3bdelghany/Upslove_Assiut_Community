Memo, Momo, k=map(int,input().split())
if Memo%k and Momo%k: print("No One")
elif Memo%k and not(Momo%k): print("Momo")
elif not(Memo%k) and Momo%k: print("Memo")
else: print("Both")