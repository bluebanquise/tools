Name:     bootset
Summary:  bootset
Release:  1%{?dist}
Version:  %{_software_version}
License:  MIT
Group:    System Environment/Base
URL:      https://github.com/bluebanquise/
Source:   https://bluebanquise.com/sources/bootset-%{_software_version}.tar.gz
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

%files
%defattr(-,root,root,-)
/usr/bin/bootset

%changelog

* Mon May 31 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Create
