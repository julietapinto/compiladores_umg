a = 10
b = 2.5
s = "hola"
arr[0] = 1
arr[1] = 2
arr[2] = 3
print a
t0 = arr[1]
print t0
x = 5
t1 = x > 0
t2 = - x
r = t2
print r
i = 0
L0:
t3 = i < 3
if t3 goto L1
goto L2
L1:
t4 = i == 1
if t4 goto L3
goto L4
L3:
goto L2
L4:
print i
t5 = i + 1
i = t5
goto L0
L2:
if x == 1 goto L5
if x == 5 goto L6
goto L7
L5:
print x
L6:
print x
L7:
print 0
L8: