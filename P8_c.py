import pandas as pd
def foo_p8_c(pr1,s1,s8,f2,p2):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=14,
                     nrows=0,
                     index_col=0))
    i=1
    list_p1 = []
    while i<9:

        s8v=s8*(0.991277737051324)**i
        cs9=961.7556
        f2p1 = -1.172828 * f2 * (1.04188579767041) ** i
        s1p1 = 0.116364 * s1 * (0.969112599877273) ** i
        pr1p1 = 0.636084 * pr1 * (0.997677094531224) ** i
        cp1 = -557.8704
        p1 = cp1 + pr1p1 + s1p1 + f2p1
        p1s9=-0.429219*p1
        cs10=349.0697
        p1s10=-0.137595*p1
        cs4=9491.33
        p1s4=-7.698679*p1
        p2s4=-1.419868*p2*(1.00405898684453)**i
        cs7=1153.679
        p2s7=-0.416872*p2*(1.00405898684453)**i
        P8_c=(s8v+cs9+p1s9+cs10+p1s10)/(cs4+p1s4+p2s4+cs7+p2s7)
        list_p1.append(P8_c)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'года': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значения':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks