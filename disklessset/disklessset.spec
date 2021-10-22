Name:     disklessset
Summary:  disklessset
Release:  2%{?dist}
Version:  %{_software_version}
License:  MIT
Group:    System Environment/Base
URL:      https://github.com/bluebanquise/
Source:   https://bluebanquise.com/sources/disklessset-%{_software_version}.tar.gz
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
cp disklessset.py $RPM_BUILD_ROOT/usr/bin/disklessset

# create /etc/disklessset/diskless_parameters.yml with default values
mkdir -p $RPM_BUILD_ROOT/etc/disklessset
cat > $RPM_BUILD_ROOT/etc/disklessset/diskless_parameters.yml << EOF
modules_path: '%{python3_sitelib}/diskless/modules'
images_directory: '/var/www/html/preboot_execution_environment/diskless/images'
EOF

# create empty /var/lib/diskless/installations.yml
mkdir -p $RPM_BUILD_ROOT/var/lib/diskless
touch $RPM_BUILD_ROOT/var/lib/diskless/installations.yml

# Create base directories for images
mkdir -p $RPM_BUILD_ROOT/var/www/html/preboot_execution_environment/diskless/{images,kernels}

# Create additional directories for images
mkdir -p $RPM_BUILD_ROOT/diskless/images/nfsimages/{golden,staging}

# Create working directory for images
mkdir -p $RPM_BUILD_ROOT/var/tmp/diskless/workdir

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/bin/disklessset
%{python3_sitelib}/diskless/*
/etc/disklessset/diskless_parameters.yml
/var/lib/diskless/installations.yml

%dir /var/www/html/preboot_execution_environment/diskless/{,images,kernels}

%dir /diskless
%dir /diskless/images
%dir /diskless/images/nfsimages/{,golden,staging}

%dir /var/tmp/diskless/workdir

%changelog
* Mon Aug 16 2021 Giacomo Mc Evoy <gino.mcevoy@gmail.com>
- Add RPM dependencies
- Install modules inside diskless/modules
- Create additional directories
- Add diskless_parameters.yml, installations.yml

* Mon May 31 2021 Benoit Leveugle <benoit.leveugle@gmail.com>
- Create
