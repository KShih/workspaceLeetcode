def maximum_time(time):
    if time[0] == "2" or time[1] <= "3" or (time[0] == "?" and time[1] == "?"):
        ret = "23:59"
    else:
        ret = "19:59"
    for i in range(len(time)):
        if time[i] != "?":
            ret = ret[:i] + time[i] + ret[i+1:]
    print ret

if __name__ == '__main__':
    maximum_time("23:5?");# 23:59
    maximum_time("2?:22");# 23:22
    maximum_time("0?:??");# 09:59
    maximum_time("1?:??");# 19:59
    maximum_time("?4:??");# 14:59
    maximum_time("?3:??");# 23:59!
    maximum_time("??:??");# 23:59
    maximum_time("?4:5?"); #14:59
    maximum_time("?4:??"); #14:59
    maximum_time("23:5?"); #23:59
    maximum_time("2?:22"); #23:22
    maximum_time("0?:??"); #09:59
    maximum_time("1?:??"); #19:59
    maximum_time("?4:0?"); #14:09
    maximum_time("?9:4?"); #19:49
