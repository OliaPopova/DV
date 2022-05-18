import pandas as pd
def foo_p7_c(pr1,s1,s2,s3,f2,p2):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=13,
                     nrows=0,
                     index_col=0))
    i=1
    list_p1 = []
    while i<9:
        cs4=9491.33
        f2p1 = -1.172828 * f2 * (1.04188579767041) ** i
        s1p1 = 0.116364 * s1 * (0.969112599877273) ** i
        pr1p1 = 0.636084 * pr1 * (0.997677094531224) ** i
        cp1 = -557.8704
        p1 = cp1 + pr1p1 + s1p1 + f2p1
        p1s4=-1.419868*p1

        p2s4=-7.698679*p2*(1.00405898684453)**i

        cs7=1153.679
        s2v=s2*(0.987953450788469)**i
        s3v=s3*(1.0089913333899)**i
        p2s7=-0.416872*p2*(1.00405898684453)**i

        P7_c=(cs4+p1s4+p2s4+cs7+p2s7)/(s2v+s3v+cs4+p1s4+p2s4+cs7+p2s7)
        list_p1.append(P7_c)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'год': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значение':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks


def foo_p7_cv(year,pr1,s1,s2,s3,f2,p2):
    df=foo_p7_c(pr1,s1,s2,s3,f2,p2)
    df_val = list(df[df['год'] == '2022'].squeeze())
    val22 = float(df_val[1])
    listval = list(df[df['год'] == year].squeeze())
    val = float(listval[1])
    mydict = {
        'год': ['2022', year],
        'значение': [val22, val]
    }
    mydf = pd.DataFrame(mydict)
    return mydf

