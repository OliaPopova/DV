import pandas as pd
from P1 import foo_p1
from P2 import foo_p2
from P3 import foo_p3
from P4 import foo_p4
from P5 import foo_p5
from P6 import foo_p6
from P1_c import foo_p1_c
from P2_c import foo_p2_c
from P3_c import foo_p3_c
from P4_c import foo_p4_c
from P5_c import foo_p5_c
from P6_c import foo_p6_c
from P7_c import foo_p7_c
from P8_c import foo_p8_c

def func(name,p2,f2,s1,pr1,p3,s5,s2,s3,f4,ar1,ar2,ar3,p4,f5,f6,s8):
    if name=='p1':
        df=foo_p1(p2,f2,s1,pr1)
        return df
    elif name=='p2':
        df = foo_p2(p3,f2,s1,pr1)
        return df
    elif name=='p3':
        df = foo_p3(s5,s2,s3,p2,f2,s1,pr1)
        return df
    elif name=='p4':
        df = foo_p4(p2,f2,s1,pr1)
        return df
    elif name=='p5':
        df = foo_p5(f4,p2,f2,s1,pr1)
        return df
    elif name=='p6':
        df = foo_p6(f4,p2,f2,s1,pr1)
        return df
    elif name=='p1c':
        df = foo_p1_c(ar1,p2,f2,s1,pr1)
        return df
    elif name=='p2c':
        df = foo_p2_c(ar2,p2,f2,s1,pr1)
        return df
    elif name=='p3c':
        df = foo_p3_c(ar3,p2,f2,s1,pr1)
        return df
    elif name=='p4c':
        df = foo_p4_c(p4,p2)
        return df
    elif name=='p5c':
        df = foo_p5_c(pr1,s1,f5,f2,p2)
        return df
    elif name=='p6c':
        df = foo_p6_c(pr1,s1,f6,f2,p2)
        return df
    elif name=='p7c':
        df = foo_p7_c(pr1,s1,s2,s3,f2,p2)
        return df
    elif name=='p8c':
        df = foo_p8_c(pr1,s1,s8,f2,p2)
        return df