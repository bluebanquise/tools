Name:     disklessset
Summary:  disklessset
Release:  1%{?dist}
Version:  %{_software_version}
License:  MIT
Group:    System Environment/Base
URL:      https://github.com/bluebanquise/
Source:   https://bluebanquise.com/sources/disklessset-%{_software_version}.tar.gz
Packager: Benoit Leveugle <benoit.leveugle@gmail.com>

%define debug_package %{nil}

%description
Disklessset tool for BlueBanquise

%prep

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{python3_sitelib}/
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp -R diskless $RPM_BUILD_ROOT/%{python3_sitelib}/
cp disklessset $RPM_BUILD_ROOT/usr/bin/disklessset

%files
%defattr(-,root,root,-)
/usr/bin/disklessset
%{python3_sitelib}/diskless/*

%changelog

* Mon May 31 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Create
