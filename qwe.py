import sqlite3


def get_result(a):
    con = sqlite3.connect('dishes.db')
    cur = con.cursor()
    t0 = []
    t1 = []
    u = {}
    r0 = f"""Select meal from Menu where volume > {a}"""
    r1 = f"""Select calories from Menu where volume > {a}"""
    t0.append(cur.execute(r0).fetchall())
    t1.append(cur.execute(r1).fetchall())
    for i in t0:
        for j in range(len(*t0)):
            try:
                if i[j]:
                    u[t1[0][j]] = i[j]
            except Exception:
                pass
    print(u)
    u1 = dict(sorted(u.items()))
    print(u1)
    u2 = list(reversed(u1.keys()))
    print(u2)
    for i in t0:
        for j in range(5):
            try:
                if i[j]:
                    print(*reversed(u1[t1[0][j]]), *u2[j])
            except Exception:
                pass
    con.commit()
    con.close()


get_result(int(input()))

