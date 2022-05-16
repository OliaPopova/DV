import pandas as pd
def foo_p1(p2,f2,s1,pr1):

    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=1,
                     nrows=0,
                     index_col=0))



    i=1
    list_p1 = []
    while i<9:
        cf1 = 1953662
        cp1 = -557.8704
        s1f = s1
        s1p = s1
        pr1f = pr1
        pr1p = pr1
        p2f=6824.962*p2*(1.00405898684453)**i
        f2p=-1.172828*f2*(1.04188579767041)**i
        s1f=-103.8427*s1f*(0.969112599877273)**i
        s1p=0.116364*s1p*(0.969112599877273)**i
        pr1f=-2517.148*pr1f*(0.997677094531224)**i
        pr1p=0.636084*pr1p*(0.997677094531224)**i
        P1=(cf1+p2f+pr1f+s1f)/(cp1+f2p+pr1p+s1p+p2)
        list_p1.append(P1)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'года': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значения':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks


def foo_p1_v(year,p2,f2,s1,pr1):
    df=foo_p1(p2,f2,s1,pr1)
    df_val = list(df[df['года'] == '2022'].squeeze())
    val22 = float(df_val[1])
    listval = list(df[df['года'] == year].squeeze())
    val = float(listval[1])
    mydict = {
        'года': ['2022', year],
        'значения': [val22, val]
    }
    mydf = pd.DataFrame(mydict)
    return mydf
