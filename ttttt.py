import pandas as pd


df_val =list( pd.read_excel(io='2015-2022.xlsx',
                     engine='openpyxl',
                     usecols='O:W',
                     header=1,
                     nrows=0,
                     index_col=0))
p2=1.1
f2=2.1
s1=3.1
pr1=4.1

i=0
cf1=1953662
cp1=-557.8704
s1f=s1p=s1
pr1f=pr1p=pr1
list_p1=[]
while i<8:
        p2=6824.962*p2*(1.00405898684453)**i
        f2=-1.172828*f2*(1.04188579767041)**i
        s1f=-103.8427*s1f*(0.969112599877273)**i
        s1p=0.116364*s1p*(0.969112599877273)**i
        pr1f=-2517.148*pr1f*(0.997677094531224)**i
        pr1p=0.636084*pr1p*(0.997677094531224)**i
        P1=(cf1+p2+pr1f+s1f)/(cp1+f2+pr1p+s1p+p2)
        list_p1.append(P1)
        i=i+1

df_val=df_val+list_p1

mydictionary = {
                'года': ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023','2024', '2025', '2026', '2027', '2028', '2029','2030'],
                'значения':df_val,
                'значения2':df_val
                    }
df_marks = pd.DataFrame(mydictionary)


print(df_marks[df_marks['года'] == '2020'].squeeze())
list_2020 = list(df_marks[df_marks['года'] == '2020'].squeeze())
list_2020.pop(0)
for x in list_2020:
    str(x)
print(type(str(list_2020)))
print(str(list_2020))
list_2020=str(list_2020)
print(type(list_2020))
print(type(list_2020[0]))


