import pandas as pd
def foo_p5(s6):
    df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=5,
                     nrows=0,
                     index_col=0))
    i=1
    list_p1 = []
    while i<9:
        s6v=s6*(1.0427680782803)**i
        P5=s6v
        list_p1.append(P5)
        i=i+1

    df_val = df_val + list_p1

    mydictionary = {
                'года': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значения':df_val
                    }
    df_marks = pd.DataFrame(mydictionary)

    return df_marks