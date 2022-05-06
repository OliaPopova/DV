import pandas as pd
def foo_p5(f4,p2,f2,s1,pr1):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=5,
                     nrows=0,
                     index_col=0))
    i=1
    list_p1 = []
    while i<9:
        f4v=f4*(0.936641510963047)**i
        cp1=-557.8704
        f2p1v=-1.172828*f2*(1.04188579767041)**i
        s1p1v=0.116364*s1*(0.969112599877273)**i
        pr1p1v=0.636084*pr1*(0.997677094531224)**i
        p2v=p2*(1.00405898684453)**i
        P5=f4v/(cp1+f2p1v+s1p1v+pr1p1v+p2v)
        list_p1.append(P5)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'года': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значения':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks