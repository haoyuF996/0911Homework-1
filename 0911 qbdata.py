with open('qbdata.txt','r') as qb:
    qbdata = qb.readlines()
    namelist = []
    ratinglist = []
    for line in qbdata:
        count = 0
        mid = 0
        while True:
            if line[count]==' ':
                    if mid==0:
                        mid+=1
                    else:
                        name=line[0:count]
                        break
            count+=1
        namelist.append(name)
        count=len(line)-1
        while True:
            if line[count]==' ':
                rating = line[count+1:-1]
                break
            count-=1
        ratinglist.append(float(rating))
    for i in range(len(namelist)):
        if ratinglist[i]>60:
            print(f'{namelist[i]} has a rating of {ratinglist[i]}')