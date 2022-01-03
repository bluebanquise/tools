Name:     bluebanquise-bootset
Summary:  bluebanquise-bootset
Release:  1%{?dist}
Version:  %{_software_version}
License:  MIT
Group:    System Environment/Base
URL:      https://github.com/bluebanquise/
Source:   https://bluebanquise.com/sources/bluebanquise-bootset-%{_software_version}.tar.gz
Packager: Benoit Leveugle <benoit.leveugle@gmail.com>

%define debug_package %{nil}

%description
Bootset tool for BlueBanquise

%prep

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp bootset $RPM_BUILD_ROOT/usr/bin/bootset
rm -f $RPM_BUILD_ROOT/usr/bin/bluebanquise-bootset
ln -s /usr/bin/bootset $RPM_BUILD_ROOT/usr/bin/bluebanquise-bootset


%files
%defattr(-,root,root,-)
/usr/bin/bootset
/usr/bin/bluebanquise-bootset

%changelog

* Mon Dec 13 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Rename
- Add symbolic link

* Mon May 31 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Create
