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

def func(year,p2,f2,s1,pr1,p3,s5,s2,s3,f4,ar1,ar2,ar3,p4,f5,f6,s8):
    dfp1 = foo_p1(p2, f2, s1, pr1)
    dfp2 = foo_p2(p3, f2, s1, pr1)
    dfp3 = foo_p3(s5, s2, s3, p2, f2, s1, pr1)
    dfp4 = foo_p4(p2, f2, s1, pr1)
    dfp5 = foo_p5(f4, p2, f2, s1, pr1)
    dfp6 = foo_p6(f4, p2, f2, s1, pr1)
    dfp1c = foo_p1_c(ar1, p2, f2, s1, pr1)
    dfp2c = foo_p2_c(ar2, p2, f2, s1, pr1)
    dfp3c = foo_p3_c(ar3, p2, f2, s1, pr1)
    dfp4c = foo_p4_c(p4, p2)
    dfp5c = foo_p5_c(pr1, s1, f5, f2, p2)
    dfp6c = foo_p6_c(pr1, s1, f6, f2, p2)
    dfp7c = foo_p7_c(pr1, s1, s2, s3, f2, p2)
    dfp8c = foo_p8_c(pr1, s1, s8, f2, p2)

    mydictionary = {
        'года': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027',
                 '2028', '2029', '2030'],
        'p1': dfp1['значения'],
        'p2': dfp2['значения'],
        'p3': dfp3['значения'],
        'p4': dfp4['значения'],
        'p5': dfp5['значения'],
        'p6': dfp6['значения'],
        'p1c': dfp1c['значения'],
        'p2c': dfp2c['значения'],
        'p3c': dfp3c['значения'],
        'p4c': dfp4c['значения'],
        'p5c': dfp5c['значения'],
        'p6c': dfp6c['значения'],
        'p7c': dfp7c['значения'],
        'p8c': dfp8c['значения']
    }
    df = pd.DataFrame(mydictionary)
    if year=="2023":
        list_2023=list(df[df['года'] == '2023'].squeeze())
        list_2023.pop(0)
        mydictionary = {
            'показатель': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            'значение':list_2023
        }
        df = pd.DataFrame(mydictionary)
        return df
    elif year=="2024":
        list_2024=list(df[df['года'] == '2024'].squeeze())
        list_2024.pop(0)
        mydictionary = {
            'показатель': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
            'значение': list_2024
        }
        df = pd.DataFrame(mydictionary)
        return df
    if year=="2025":
        list_2025=list(df[df['года'] == '2025'].squeeze())
        list_2025.pop(0)

        mydictionary = {
            'показатель': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            'значение': list_2025
        }
        df = pd.DataFrame(mydictionary)
        return df
    if year=="2026":
        list_2026=list(df[df['года'] == '2026'].squeeze())
        list_2026.pop(0)
        mydictionary = {
            'показатель': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
            'значение': list_2026
        }
        df = pd.DataFrame(mydictionary)
        return df
    if year=="2027":
        list_2027=list(df[df['года'] == '2027'].squeeze())
        list_2027.pop(0)
        mydictionary = {
            'показатель': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
            'значение': list_2027
        }
        df = pd.DataFrame(mydictionary)
        return df
    if year=="2028":
        list_2028=list(df[df['года'] == '2028'].squeeze())
        list_2028.pop(0)
        mydictionary = {
            'показатель': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            'значение': list_2028
        }
        df = pd.DataFrame(mydictionary)
        return df
    if year=="2029":
        list_2029=list(df[df['года'] == '2029'].squeeze())
        list_2029.pop(0)
        mydictionary = {
            'показатель': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            'значение': list_2029
        }
        df = pd.DataFrame(mydictionary)
        return df
    if year=="2030":
        list_2030=list(df[df['года'] == '2030'].squeeze())
        list_2030.pop(0)
        mydictionary = {
            'показатель': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
            'значение': list_2030
        }
        df = pd.DataFrame(mydictionary)
        return df

