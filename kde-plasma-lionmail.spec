%global applet_name lionmail

Name:           kde-plasma-lionmail
Version:        0.1
Release:        1%{?dist}.R
Summary:        Email notifier plasmoid

Group:          User Interface/Desktops
License:        GPLv2+
URL:            https://projects.kde.org/projects/playground/base/plasma-lionmail
Source0:        plasma-lionmail-0.1.tar.bz2

BuildRequires:  cmake gettext kdebase-workspace-devel kdepimlibs-devel akonadi-devel kdelibs-devel

%description
Email notifier plasmoid.


%prep
%setup -q -n plasma-%{applet_name}-%{version}


%build
%{cmake_kde4}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_libdir}/kde4/plasma_applet_*.so
%{_datadir}/kde4/apps/plasma/plasmoids/*
%{_datadir}/kde4/services/plasma-applet-*.desktop


%changelog
* Sun Jan 15 2012 Alexey Torkhov <atorkhov@gmail.com> - 0.1-1.R
- Initial package.

