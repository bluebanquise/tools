#!/usr/bin/bash

set -x

source versions.conf

cp -a bluebanquise-bootset bluebanquise-bootset-$bluebanquise_bootset_version
tar cvzf bluebanquise-bootset-$bluebanquise_bootset_version.tar.gz bluebanquise-bootset-$bluebanquise_bootset_version
rpmbuild -ta bluebanquise-bootset-$bluebanquise_bootset_version.tar.gz --define "_software_version $bluebanquise_bootset_version" --target=noarch
rm -Rf bluebanquise-bootset-$bluebanquise_bootset_version bluebanquise-bootset-$bluebanquise_bootset_version.tar.gz

#python3 -c "import site; print(site.getsitepackages()[0])"
cp -a bluebanquise-disklessset bluebanquise-disklessset-$bluebanquise_disklessset_version
tar cvzf bluebanquise-disklessset-$bluebanquise_disklessset_version.tar.gz bluebanquise-disklessset-$bluebanquise_disklessset_version
rpmbuild -ta bluebanquise-disklessset-$bluebanquise_disklessset_version.tar.gz --define "_software_version $bluebanquise_disklessset_version" --target=noarch
rm -Rf bluebanquise-disklessset-$bluebanquise_disklessset_version bluebanquise-disklessset-$bluebanquise_disklessset_version.tar.gz

cp -a bluebanquise-filters bluebanquise-filters-$bluebanquise_filters_version
tar cvzf bluebanquise-filters-$bluebanquise_filters_version.tar.gz bluebanquise-filters-$bluebanquise_filters_version
rpmbuild -ta bluebanquise-filters-$bluebanquise_filters_version.tar.gz --define "_software_version $bluebanquise_filters_version" --target=noarch
rm -Rf bluebanquise-filters-$bluebanquise_filters_version bluebanquise-filters-$bluebanquise_filters_version.tar.gz
