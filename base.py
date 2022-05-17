
def func(selected_P2, selected_P3, selected_P4,
         selected_F2,selected_F4, selected_F5, selected_F6,
         selected_S1,selected_S2, selected_S3, selected_S5, selected_S6,selected_S8,
         selected_Pr1, selected_Ar1, selected_Ar2,selected_Ar3):

    if selected_P2 !=0:
        p2=selected_P2
    else:
        p2 = 400

    if selected_P3 !=0:
        p3=selected_P3
    else:
        p3 = 625

    if selected_P4 !=0:
        p4=selected_P4
    else:
        p4 = 400

    if selected_F2 !=0:
        f2=selected_F2
    else:
        f2 = 575

    if selected_F4 !=0:
        f4=selected_F4
    else:
        f4 = 75500

    if selected_F5 !=0:
        f5=selected_F5
    else:
        f5 = 300000

    if selected_F6 !=0:
        f6=selected_F6
    else:
        f6 = 5000

    if selected_S1 !=0:
        s1=selected_S1
    else:
        s1 = 25000

    if selected_S2 !=0:
        s2=selected_S2
    else:
        s2 = 11500

    if selected_S3 !=0:
        s3=selected_S3
    else:
        s3 = 1550

    if selected_S5 !=0:
        s5=selected_S5
    else:
        s5 = 1750

    if selected_S6 !=0:
        s6=selected_S6
    else:
        s6 = 4500

    if selected_S8 !=0:
        s8=selected_S8
    else:
        s8 = 125

    if selected_Pr1 !=0:
        pr1=selected_Pr1
    else:
        pr1 = 195

    if selected_Ar1 !=0:
        ar1=selected_Ar1
    else:
        ar1 = 250

    if selected_Ar2 !=0:
        ar2=selected_Ar2
    else:
        ar2 = 350

    if selected_Ar3 !=0:
        ar3=selected_Ar3
    else:
        ar3 = 50

    return p2,p3,p4,f2,f4,f5,f6,s1,s2,s3,s5,s6,s8,pr1,ar1,ar2,ar3

