Records for each and every building in Iceland.

Each record contains a *landnúmer* and a *heitinúmer* (more on these below), a
street address, a post code, and a longitude and latitude. The longitude and
latitude denote the centre point of the building.

A *landnúmer* is a unique identifer for each plot of land containing one or more
buildings; every such plot in the country has one of these ids. They're
maintained by [Þjóðskrá Íslands] [1], the National Registry of Iceland.

Each building in the country should in theory be uniquely identifiable by a its
street address and *landnúmer*, although in practice this isn't true because the
data isn't reliable enough. Hence the *heitinúmer* — a building id — also
provided by Þjóðskrá, which does uniquely identify a building.

OK, that's a lie too. I think the *heitinúmer* should be unique to an individual
building, but there are errors in the data that stop this being true. For
example, [Stóru-Grafarland 134985] [2] is a collection of summer houses that
really should have separate *heitinúmer*, but don't.

This file is a version of the Staðfangaskrá (address registry) provided by
Þjóðskrá, whittled down to a useful minimum and with duplicate records removed.

The source is [available from the Icelandic government's open data portal] [3],
and is released under an (unspecified) open data licence.

## Data description

This data is provided as a [Data Package] [4]. The data itself can be found in
`data/landnr.json`; the Python code that created it is in `scripts/collect.py`;
a description of the data, including a [JSON Table Schema] [5], can be found in
`datapackage.json`.

The data is JSON, provided as an array of objects. Each object in the array
corresponds to a building and is in the following format:

    {
      "landnr": 105983,
      "heitinr": 1000864,
      "street": "Aflagrandi 21",
      "postcode": 107
      "ll": [
        -21.961317,
        64.147867
      ],
    },

Definitions of each attribute in an object:

* **landnr**: the *landnúmer* (land plot id) for the plot on which the building
  stands; always an integer
* **heitinr**: the *heitinúmer* (building id) for the building itself; always an
  integer
* **street**: the name of the street the building in on, and the building's
  street number; always a string
* **postcode**: the building's post code; always an integer
* **ll**: an array of longitude and latitude; always a [geopoint] [6]

[1]: http://skra.is/
[2]: http://skra.is/Pages/1000?landnr=134985&streetname=St%C3%B3ru-Grafarland%20134985
[3]: http://opingogn.is/dataset/stadfangaskra
[4]: http://www.dataprotocols.org/en/latest/data-packages.html
[5]: http://www.dataprotocols.org/en/latest/json-table-schema.html
[6]: http://www.dataprotocols.org/en/latest/json-table-schema.html#types
