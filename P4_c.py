import pandas as pd
def foo_p4_c(p4,p2):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=10,
                     nrows=0,
                     index_col=0))
    i=1
    list_p1 = []
    while i<9:
        p4v=p4*(1.07064878325541)**i

        p2v=p2*(1.00405898684453)**i
        if p2v == 0:
            P4_c=0
        else:
            P4_c=p4v/p2v
        list_p1.append(P4_c)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'год': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значение':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks

def foo_p4_cv(year,p4,p2):
    df=foo_p4_c(p4,p2)
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
