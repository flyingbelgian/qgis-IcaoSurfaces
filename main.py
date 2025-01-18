import csv

import conversions as convert


runways = {}

with open("runway.csv", "r") as file:
    csvFile = csv.reader(file)
    # Skip first line of csv
    firstline = True
    for line in csvFile:
        if not firstline:
            rwy = line[0]
            startX = float(line[1])
            startY = float(line[2])
            start = (startX,startY)
            endX = float(line[3])
            endY = float(line[4])
            end = (endX,endY)
            appX = float(line[5])
            appY = float(line[6])
            app = (appX,appY)
            thrX = float(line[7])
            thrY = float(line[8])
            thrZ = float(line[9])
            thr = (thrX,thrY)
            thr3D = (thrX,thrY,thrZ)
            if line[10] and line[11]:
                swyX = float(line[10])
                swyY = float(line[11])
                swy = (swyX,swyY)
            else:
                swy = False
            cwyX = float(line[12])
            cwyY = float(line[13])
            cwyZ = float(line[14])
            cwy = (cwyX,cwyY)
            cwy3D = (cwyX,cwyY,cwyZ)
            refsystem = convert.define_reference_system(thr,end)

            runways[rwy] = {
                "start":start,
                "end":end,
                "app":app,
                "thr":thr,
                "thr3D":thr3D,
                "swy":swy,
                "cwy":cwy,
                "cwy3D":cwy3D,
                "refsystem":refsystem
            }
        else:
            firstline = False


# for rwy, data in runways.items():
#     tora = convert.distance_2pts(data['start'],data['end'])
#     toda = convert.distance_2pts(data['start'],data['cwy'])
#     if data['swy']:
#         asda = convert.distance_2pts(data['start'],data['swy'])
#     else:
#         asda = tora
#     lda = convert.distance_2pts(data['thr'],data['end'])
#     print(f"Runway {rwy}:")
#     print(f"   TORA: {round(tora,1)}m")
#     print(f"   TODA: {round(toda,1)}m")
#     print(f"   ASDA: {round(asda,1)}m")
#     print(f"   LDA : {round(lda,1)}m")
    

obstacles = {}

with open("obstacles.csv", "r") as file:
    csvFile = csv.reader(file)
    # Skip first line of csv
    firstline = True
    for line in csvFile:
        if not firstline:
            obst_id = line[0]
            obst_coords = (float(line[1]),float(line[2]))
            obstacles[obst_id] = {}
            for rwy,data in runways.items():
                namerwyxy = str(rwy)+"_xy"
                obstacles[obst_id][namerwyxy] = convert.convert_to_xy(obst_coords,data['refsystem'])
        else:
            firstline = False

for obstacle,data in obstacles.items():
    print(obstacle)
    print(data)

# obstacledata = []
# for data in obstacles.values():
#     obstacledata.append(
#         {}
#     )

# with open('obstacles_xy.csv', 'w', newline='') as file:
#     fieldnames = ['id']
#     for obstacle in obstacles.keys():
#         fieldnames.append(obstacle)
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
