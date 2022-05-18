import pandas as pd
def foo_p3_c(ar3,p2,f2,s1,pr1):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=9,
                     nrows=0,
                     index_col=0))
    i=1
    list_p1 = []
    while i<9:
        ar3v=ar3*(0.952912293694355)**i
        cp1=-557.8704
        f2p1v=-1.172828*f2*(1.04188579767041)**i
        s1p1v=0.116364*s1*(0.969112599877273)**i
        pr1p1v=0.636084*pr1*(0.997677094531224)**i
        p2v=p2*(1.00405898684453)**i
        P3_c=ar3v/(cp1+f2p1v+s1p1v+pr1p1v+p2v)
        list_p1.append(P3_c)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'год': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значение':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks

def foo_p3_cv(year,ar3,p2,f2,s1,pr1):
    df=foo_p3_c(ar3,p2,f2,s1,pr1)
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

