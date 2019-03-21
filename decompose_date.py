def decompose_date(df, analyse_col):
    print(analyse_col)
    import pandas as pd
    clean_col = analyse_col.replace(" ", "_")
    from collections import OrderedDict
    weekdays = OrderedDict( {0: "lundi", 1: "mardi", 2: "mercredi", 
                             3: "jeudi", 4: "vendredi", 5: "samedi", 6: "dimanche"})
    mois = OrderedDict({1: "janvier"  , 2: "février" ,  3: "mars", 4: "avril", 5: "mai", 
                        6: "juin"     , 7: "juillet" ,  8: "août",
                        9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"})
    filtre = ~df[analyse_col].isnull()
    #
    new_col     = "%s_jour_semaine" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: x.weekday()).map(weekdays)
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=weekdays.values(), ordered=True)
    #
    new_col     = "%s_jour_semaine_int" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[analyse_col].map(lambda x: x.weekday())

    #
    new_col = "%s_jour_mois" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: x.day)
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=range(32), ordered=True)

    #
    new_col = "%s_mois" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: x.month).map(mois)
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=mois.values(), ordered=True)
    #
    new_col = "%s_nth_mois" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: x.month)
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=range(1, 13), ordered=True)
    #
    new_col = "%s_nth_semestre" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: 1 if x.month<7 else 2)
    #
    new_col = "%s_nth_quarter" % clean_col
    print(new_col)
    
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: int(1 + (x.month-1)//3 ))
    
    #
    new_col = "%s_week" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: int(x.week))
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=range(53), ordered=True)

    #
    new_col = "%s_year" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: int(x.year))
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=sorted(list(df[filtre][new_col].unique())), ordered=True)
    #
    new_col = "%s_nth_day" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][analyse_col].map(lambda x: x.timetuple().tm_yday)
    df.loc[filtre, new_col] = pd.Categorical(df[filtre][new_col], categories=range(366), ordered=True)
    #
    year    = "%s_year" % clean_col
    nth_day = "%s_nth_day" % clean_col
    new_col = "%s_year_plus_day" % clean_col
    print(new_col)
    df.loc[filtre, new_col] = df[filtre][year] + (df[filtre][nth_day]  / 365)
    
    print("fini")
