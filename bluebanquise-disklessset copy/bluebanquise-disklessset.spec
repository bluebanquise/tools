Name:     bluebanquise-disklessset
Summary:  bluebanquise-disklessset
Release:  1%{?dist}
Version:  %{_software_version}
License:  MIT
Group:    System Environment/Base
URL:      https://github.com/bluebanquise/
Source:   https://bluebanquise.com/sources/bluebanquise-disklessset-%{_software_version}.tar.gz
Packager: Benoit Leveugle <benoit.leveugle@gmail.com>

%define debug_package %{nil}

Requires: httpd
Requires: python3-clustershell
Requires: nfs-utils
Requires: dracut-live
Requires: xfsdump

%if 0%{?rhel} == 9
Requires: squashfs-tools
%endif

%description
Disklessset tool for BlueBanquise

%prep

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{python3_sitelib}/diskless/modules
cp -R diskless $RPM_BUILD_ROOT/%{python3_sitelib}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/diskless/*_module.py $RPM_BUILD_ROOT/%{python3_sitelib}/diskless/modules

mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp disklessset $RPM_BUILD_ROOT/usr/bin/disklessset
rm -f $RPM_BUILD_ROOT/usr/bin/bluebanquise-disklessset
ln -s /usr/bin/disklessset $RPM_BUILD_ROOT/usr/bin/bluebanquise-disklessset

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/bin/disklessset
/usr/bin/bluebanquise-disklessset
%{python3_sitelib}/diskless/*

%changelog

* Mon Dec 13 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Rename
- Remove Ansible dedicated part
- Add symbolic link

* Mon Oct 18 2021 David Pieters <davidpieters22@gmail.com>
- Diskless tool v1.3.0 update, it includes:
- Add clone system.
- Add create image from parameters file system.
- Review display system.
- Review questions system and menu.
- Add info mode and debug mode command.

* Mon Aug 16 2021 Giacomo Mc Evoy <gino.mcevoy@gmail.com>
- Add RPM dependencies
- Install modules inside diskless/modules
- Create additional directories
- Add diskless_parameters.yml, installations.yml

* Mon May 31 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Create
