import pandas as pd
def foo_p2(p3,f2,s1,pr1):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=2,
                     nrows=0,
                     index_col=0))


    i=1
    list_p1 = []
    while i<9:
        c=-557.8704
        p3v=p3*(0.974045952199263)**i
        f2v=-1.172828*f2*(1.04188579767041)**i
        s1v=0.116364*s1*(0.969112599877273)**i
        pr1v=0.636084*pr1*(0.997677094531224)**i
        P2=p3v/(c+f2v+s1v+pr1v)
        list_p1.append(P2)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'года': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значения':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks

def foo_p2_v(year,p3,f2,s1,pr1):
    df=foo_p2(p3,f2,s1,pr1)
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