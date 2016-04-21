%define        _topdir  %{rpmbuild}
%define        _tmppath %{_topdir}/tmp

Summary: Tool for managing remote & local storage.
Name: poly
Version: %{v_semver}
Release: 1
License: Apache License
Group: Applications/Storage
#Source: https://github.com/dvonthenen/poly/archive/master.zip
URL: https://github.com/dvonthenen/poly
Vendor: EMC{code}
Packager: Andrew Kutz <sakutz@gmail.com>
BuildArch: %{v_arch}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
A guest based storage introspection tool that
allows local visibility and management from cloud
and storage platforms.

%prep

%build

%install
install -D %{poly} $RPM_BUILD_ROOT/usr/bin/poly

%post
/usr/bin/poly install 1> /dev/null

%preun
/usr/bin/poly uninstall --package 1> /dev/null

%clean
#rm -rf "$RPM_BUILD_ROOT"

%files
%attr(0755, root, root) /usr/bin/poly
