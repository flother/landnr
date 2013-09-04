Minimal data on Icelandic landnúmer.

A landnúmer is a unique identifer for each plot of land containing a building;
every such plot in the country has one of these ids. They're maintained by
Þjóðskrá, the National Registry of Iceland.

Each building in the country can be uniquely identified by its street address
and landnúmer. This data package contains a record for each building; a
landnúmer is not necessarily unique (if there are three buildings on a plot of
land, for example, the buildings will share the landnúmer) but the combination
of street address and landnúmer is.

Each record includes a "thjodskra_id", which contains the unique building id
used by Þjóðskrá. This will always have a one-to-one relationship with the
street address and landnúmer pair.

This file is a version of the Staðfangaskrá (address registry) provided by
Þjóðskrá, whittled down to a bare minimum. Each record contains five fields:
landnúmer, Þjóðskrá id, street address, post code, and longitude and latitude.

The source is [available from the Icelandic government's open data portal] [1],
and is released under an (unspecified) open data licence.

[1]: http://opingogn.is/dataset/stadfangaskra
