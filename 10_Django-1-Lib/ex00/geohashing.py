from antigravity import geohash
import sys

def geohashing(latitude, longitude, datedow):
    data = {}
    data['latitude'] = float(latitude)
    data['longitude'] = float(longitude)
    data['datedow'] = datedow.encode()
    geohash(**data)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        try:
            geohashing(sys.argv[1], sys.argv[2], sys.argv[3])
        except Exception as e:
            print(e)
    else:
        print("Use: geohashing.py <Latitude> <Longitude> <DateDow>")
