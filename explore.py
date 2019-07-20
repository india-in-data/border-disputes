import fiona
import geojsonio
import json
import sys

shape = fiona.open(sys.argv[1])
south_asia = [shp for shp in shape if shp['properties']['NOTE_BRK'] and shp['properties']['NOTE_BRK'].find('India') >= 0]
for shp in south_asia:
    dest = (shp['properties']['BRK_NAME'] + '_' + shp['properties']['NOTE_BRK'] + '.json').replace(' ', '_')
    with open(dest, 'w') as handle:
        handle.write(json.dumps(dest, indent=4))