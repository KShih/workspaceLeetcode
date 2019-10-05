import re
def rename(input):
    # Jeff_Taichung_20190804.jpg
    pattern = re.compile("([a-zA-z]+)_([a-zA-z]+)_([\d]+).(.+)")
    detailList = list()
    for pic in li:
        #pic = re.sub('[^a-zA-Z0-9 \n\.]', ' ', pic) # pic = Jeff Taichung 20190804.jpg
        split_pic = pattern.search(pic)
        picDetail = list()
        if split_pic:
            picDetail.append(split_pic.group(2)) # Location
            picDetail.append(split_pic.group(3)) # Time
            picDetail.append(split_pic.group(1)) # Name
            picDetail.append(split_pic.group(4)) # format
        detailList.append(picDetail)

    sortedDetailList = sorted(detailList, key=lambda k: (k[0],k[1]))

    locDic = dict()
    for entry in sortedDetailList:
        if entry[0] in locDic.keys():
            locDic[entry[0]].append(entry)
        else:
            locDic[entry[0]] = []
            locDic[entry[0]].append(entry)

    out = []
    for location in locDic:
        zero_counter = 0
        locCounter = len(locDic[location])
        while locCounter > 0:
            locCounter //= 10
            zero_counter += 1
        pic_counter = 0

        for pic in locDic[location]:
            pic_counter += 1
            num_zero = zero_counter - pic_counter//10
            str_zero = "0" * num_zero
            out.append(pic[0]+"_"+str_zero+str(pic_counter)+"_"+pic[2]+"."+pic[3])
    print(out)

if __name__ == "__main__":
    input = "Jeff_Taichung_20190804.jpg Ian_Taipei_20190801.jpg Eason_Taichung_20190802.png"
    # output: ['Taichung_01_Eason.png', 'Taichung_02_Jeff.jpg', 'Taipei_01_Ian.jpg']
    rename(input)
