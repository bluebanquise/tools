Name:     bluebanquise_filters
Summary:  bluebanquise_filters
Release:  1%{?dist}
Version:  %{_software_version}
License:  MIT
Group:    System Environment/Base
URL:      https://github.com/bluebanquise/
Source:   https://bluebanquise.com/sources/bluebanquise_filters-%{_software_version}.tar.gz
Packager: Benoit Leveugle <benoit.leveugle@gmail.com>

%define debug_package %{nil}

Requires: python3-clustershell

%description
Set of filters for the BlueBanquise stack

%prep

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/ansible/plugins/filter/
cp nodeset.py $RPM_BUILD_ROOT/usr/share/ansible/plugins/filter/nodeset.py

%files
%defattr(-,root,root,-)
/usr/share/ansible/plugins/filter/nodeset.py

%changelog

* Mon May 31 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Create
