Records for each and every building in Iceland.

Each record contains a landnúmer and a heitinúmer (more on these below), a
street address, a post code, and a longitude and latitude. The longitude and
latitude denote the centre point of the building.

A landnúmer is a unique identifer for each plot of land containing one or more
buildings; every such plot in the country has one of these ids. They're
maintained by Þjóðskrá, the National Registry of Iceland.

Each building in the country should in theory be uniquely identifiable by a its
street address and landnúmer, although in practice this isn't true because the
data isn't reliable enough. Hence the heitinúmer — a building id — also provided
by Þjóðskrá, which does uniquely identify a building.

OK, that's a lie too. I think the heitinúmer *should* be unique to an individual
building, but there are errors in the data that stop this being true. For
example, [Stóru-Grafarland 134985] [1] is a collection of summer houses that
really should have separate heitinúmer, but don't.

This file is a version of the Staðfangaskrá (address registry) provided by
Þjóðskrá, whittled down to a useful minimum and with duplicate records removed.

The source is [available from the Icelandic government's open data portal] [2],
and is released under an (unspecified) open data licence.

[1]: http://skra.is/Pages/1000?landnr=134985&streetname=St%C3%B3ru-Grafarland%20134985
[2]: http://opingogn.is/dataset/stadfangaskra
