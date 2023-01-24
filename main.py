import DBFtoCSV as db
import dayinter as di
import interpolator as ip
import harryplotter as hp
import pandas as pd
import sys


funcsele = sys.argv[1]
if funcsele == "1":
    path = sys.argv[2]
    db.DBFtoCSV(path).main()
elif funcsele == "2":
    path = sys.argv[2]
    dfn = pd.read_csv(path)
    x = dfn[sys.argv[3]]
    y = dfn[sys.argv[4]]
    done = pd.DataFrame(di.dayinter(x, y).main())
    done.to_csv(r".\dayinterpolated.csv")
elif funcsele == "3":
    dfn1 = pd.read_csv(sys.argv[2])
    dfn2 = pd.read_csv(sys.argv[3])
    newdf = pd.DataFrame(ip.interpolator(dfn1, dfn2).main())
    newdf.to_csv(r".\interpolated.csv")
