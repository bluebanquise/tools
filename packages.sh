#!/usr/bin/bash

set -x

source versions.conf

cp -a bluebanquise-bootset bluebanquise-bootset-$bluebanquise-bootset_version
tar cvzf bluebanquise-bootset-$bluebanquise-bootset_version.tar.gz bluebanquise-bootset-$bluebanquise-bootset_version
rpmbuild -ta bluebanquise-bootset-$bluebanquise-bootset_version.tar.gz --define "_software_version $bluebanquise-bootset_version" --target=noarch
rm -Rf bluebanquise-bootset-$bluebanquise-bootset_version bluebanquise-bootset-$bluebanquise-bootset_version.tar.gz

cp -a bluebanquise-disklessset bluebanquise-disklessset-$bluebanquise-disklessset_version
tar cvzf bluebanquise-disklessset-$bluebanquise-disklessset_version.tar.gz bluebanquise-disklessset-$bluebanquise-disklessset_version
rpmbuild -ta bluebanquise-disklessset-$bluebanquise-disklessset_version.tar.gz --define "_software_version $bluebanquise-disklessset_version" --target=noarch
rm -Rf bluebanquise-disklessset-$bluebanquise-disklessset_version bluebanquise-disklessset-$bluebanquise-disklessset_version.tar.gz

cp -a bluebanquise-filters bluebanquise-filters-$bluebanquise-filters_version
tar cvzf bluebanquise-filters-$bluebanquise-filters_version.tar.gz bluebanquise-filters-$bluebanquise-filters_version
rpmbuild -ta bluebanquise-filters-$bluebanquise-filters_version.tar.gz --define "_software_version $bluebanquise-filters_version" --target=noarch
rm -Rf bluebanquise-filters-$bluebanquise-filters_version bluebanquise-filters-$bluebanquise-filters_version.tar.gz
