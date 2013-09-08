from cStringIO import StringIO
import json
import math
import os
import sys
import zipfile

import requests
import unicodecsv


BUILDING_DATA_URL = "http://skra.is/lisalib/getfile.aspx?itemid=8424"


def get_url_content(url):
    """Returns the response content of the given URL."""
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()
    return response.content


def unzip(zip_contents):
    """Returns the given string, unzipped."""
    zip_file = zipfile.ZipFile(StringIO(zip_contents))
    filenames = zip_file.namelist()
    if len(filenames) == 1:
        data = zip_file.open(filenames[0], "rU")
        return data
    raise ValueError("zip file contains %d files" % len(filenames))


def iter_rows(building_data):
    """
    Opens the given file-like object as a CSV file delimited by pipes,
    and yields a list for each row containing the land plot number,
    building id, street address, post code, and latitude, and longitude.
    """
    reader = unicodecsv.reader(building_data, delimiter="|", encoding="latin1")
    reader.next()  # Skip header row.
    for row in reader:
        land_plot_number = int(row[3])
        building_id = int(row[4])
        street_address = u" ".join(row[5].split())  # Normalise whitespace.
        try:
            post_code = int(row[7])
        except ValueError:
            post_code = None
        isn93_x = float(row[22].replace(",", "."))
        isn93_y = float(row[23].replace(",", "."))
        longitude, latitude = isnet93_to_wgs84(isn93_x, isn93_y)
        yield {
            "landnr": land_plot_number,
            "heitinr": building_id,
            "street": street_address,
            "postcode": post_code,
            "ll": (longitude, latitude),
        }


def isnet93_to_wgs84(xx, yy):
    """
    Converts a ISN93 x and y coordinate to longitude and latitude.

    This function has been floating around the Internet for a few years
    now; the oldest reference I can find is here:

    https://gist.github.com/avar/585850
    """
    a = 6378137.0
    f = 1 / 298.257222101
    lat1 = 64.25
    lat2 = 65.75
    latc = 65.00
    lonc = 19.00
    eps = 0.00000000001

    def fx(p):
        return a * math.cos(p / rho) / math.sqrt(1 - math.pow(e * math.sin(p / rho), 2))

    def f1(p):
        return math.log((1 - p) / (1 + p))

    def f2(p):
        return f1(p) - e * f1(e * p)

    def f3(p):
        return pol1 * math.exp((f2(math.sin(p / rho)) - f2sin1) * sint / 2)

    rho = 45 / math.atan2(1.0, 1.0)
    e = math.sqrt(f * (2 - f))
    dum = f2(math.sin(lat1 / rho)) - f2(math.sin(lat2 / rho))
    sint = 2 * (math.log(fx(lat1)) - math.log(fx(lat2))) / dum
    f2sin1 = f2(math.sin(lat1 / rho))
    pol1 = fx(lat1) / sint
    polc = f3(latc) + 500000.0
    peq = a * math.cos(latc / rho) / (sint * math.exp(sint * math.log((45 - latc / 2) / rho)))
    pol = math.sqrt(math.pow(xx - 500000, 2) + math.pow(polc - yy, 2))
    lat = 90 - 2 * rho * math.atan(math.exp(math.log(pol / peq) / sint))
    lon = 0
    fact = rho * math.cos(lat / rho) / sint / pol
    fact = rho * math.cos(lat / rho) / sint / pol
    delta = 1.0
    while math.fabs(delta) > eps:
        delta = (f3(lat) - pol) * fact
        lat += delta
    lon = -(lonc + rho * math.atan((500000 - xx) / (polc - yy)) / sint)

    return round(lon, 6), round(lat, 6)


if __name__ == "__main__":
    print "Downloading data ..."
    zip_contents = get_url_content(BUILDING_DATA_URL)
    print "Unzipping data ..."
    building_data = unzip(zip_contents)
    print "Parsing data ..."
    buildings = []
    unique_buildings = set()
    for building in iter_rows(building_data):
        building_attrs = (
            hash(building["landnr"]) ^
            hash(building["heitinr"]) ^
            hash(building["street"]) ^
            hash(building["postcode"]) ^
            hash(building["ll"])
        )
        if building_attrs in unique_buildings:
            print >> sys.stderr, "Skipping duplicate row: %s." % building
        else:
            buildings.append(building)
            unique_buildings.add(building_attrs)
    # Save the building data as a JSON file.
    base_path = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(base_path, "..", "data",
        "landnr.json"))
    print "Saving data to file ..."
    fp = open(file_path, "w")
    json.dump(buildings, fp, indent=2, separators=(",", ": "))
    fp.close()
    print "Done."
