#!/usr/bin/bash

set -x

source versions.conf

cp -a bootset bootset-$bootset_version
tar cvzf bootset-$bootset_version.tar.gz bootset-$bootset_version
rpmbuild -ta bootset-$bootset_version.tar.gz --define "_software_version $bootset_version" --target=noarch
rm -Rf bootset-$bootset_version bootset-$bootset_version.tar.gz

cp -a disklessset disklessset-$disklessset_version
tar cvzf disklessset-$disklessset_version.tar.gz disklessset-$disklessset_version
rpmbuild -ta disklessset-$disklessset_version.tar.gz --define "_software_version $disklessset_version" --target=noarch
rm -Rf disklessset-$disklessset_version disklessset-$disklessset_version.tar.gz

cp -a bluebanquise_filters bluebanquise_filters-$bluebanquise_filters_version
tar cvzf bluebanquise_filters-$bluebanquise_filters_version.tar.gz bluebanquise_filters-$bluebanquise_filters_version
rpmbuild -ta bluebanquise_filters-$bluebanquise_filters_version.tar.gz --define "_software_version $bluebanquise_filters_version" --target=noarch
rm -Rf bluebanquise_filters-$bluebanquise_filters_version bluebanquise_filters-$bluebanquise_filters_version.tar.gz
