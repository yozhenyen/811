import pandas as pd
mon = 1
day = 1


def alltime(i, j, k):
    global mon
    global day
    list = []
    for m in range(0, 28):
        if j % 4 != 0:
            if x == (1 or 3 or 5 or 7 or 8 or 10 or 12) and (y <= 31):
                time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
                list.append(time)
                y = y + 1
                if y > 31:
                    x = x + 1
                    y = 1
            if (x == 2) and (y <= 28):
                time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
                list.append(time)
                y = y + 1
                if y > 28:
                    x = x + 1
                    y = 1
            if ((x <= 7 and x % 2 != 1) or (x >= 8 and x % 2 != 0)) and (y <= 30):
                time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
                list.append(time)
                y = y + 1
                if y > 30:
                    x = x + 1
                    y = 1
        if j % 4 == 0:
            if ((x <= 7 and x % 2 == 1) or (x >= 8 and x % 2 == 0)) and (y <= 31):
                time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
                list.append(time)
                y = y + 1
                if y > 31:
                    x = x + 1
                    y = 1
            if (x == 2) and (y <= 29):
                time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
                list.append(time)
                y = y + 1
                if y > 29:
                    x = x + 1
                    y = 1
            if ((x <= 7 and x % 2 != 1) or (x >= 8 and x % 2 != 0)) and (y <= 30):
                time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
                list.append(time)
                y = y + 1
                if y > 30:
                    x = x + 1
                    y = 1
    df_time = np.reshape(list, (-1, 1), order='C')
    df_time = pd.DataFrame(df_time)  # 時間




#for year in range(2012,8):


