'''locmap = {}

locmap[(144,144)] = 1

#Use several digits from the position information to represent an intersection
#eg; 144,144
while locmap[(144,144)] < 4:
    locmap[(144,144)] += 1

print(locmap)'''

import serial

try:
    #cd /dev
    # ls tty.*
    gps = serial.Serial('/dev/tty.usbmodem145101', baudrate=9600)
    dic = {}
    while True:
        ser_bytes = gps.readline()
        decoded_bytes = ser_bytes.decode("utf-8")
        data = decoded_bytes.split(",")
        #print(data)
        if data[0] == "$GPRMC":
            lat_nmea = data[3]
            lat_degrees = lat_nmea[:2]
            if data[4] == 'S':
                latitude_degrees = float(lat_degrees) * -1
            else:
                latitude_degrees = float(lat_degrees)
            latitude_degrees = str(latitude_degrees).strip('.')
            lat_ddd = lat_nmea[2:10]
            lat_mmm = float(lat_ddd) / 60
            lat_mmm = str(lat_mmm).strip('0.')[:8]
            latitude = latitude_degrees +lat_mmm

            long_nmea = data[5]
            long_degrees = long_nmea[:3]
            if data[6] == "W":
                longitude_degrees = float(long_degrees) * -1
            else:
                longitude_degrees = float(long_degrees)

            longitude_degrees = str(longitude_degrees).strip('.0')
            long_ddd = long_nmea[3:10]
            long_mmm = float(long_ddd) / 60
            long_mmm = str(long_mmm).strip('0.')[:8]
            longitude = longitude_degrees + "." + long_mmm
            coordinate = [latitude, longitude]
            print("Lat is "+coordinate[0]+" Lon is",coordinate[1])
            filename = 'data.txt'

            with open(filename,'a') as f:
                f.write(str(coordinate)+'\n')

            intersection = {}

            dic[coordinate[0]+','+coordinate[1]] = 1
            if len(dic) == 10:
                break
    #print(dic)

except serial.SerialException:
    print("No connection")

