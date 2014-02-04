%define		_state		stable
%define		orgname		parley

Summary:	K Desktop Environment - program to help you memorize things
Summary(pl.UTF-8):	K Desktop Environment - program pomagający w zapamiętywaniu
Name:		kde4-parley
Version:	4.12.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	3626b1867f508fbe88de8a7a9a988561
URL:		http://www.kde.org/
BuildRequires:	attica-devel
BuildRequires:	automoc4
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdeedu-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	qt4-build
Obsoletes:	kde4-kdeedu-parley < 4.7.0
Obsoletes:	parley <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parley is a KDE program to help you memorize things.

%description -l pl.UTF-8
Parley to program dla KDE pomagający w zapamiętywaniu.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/parley
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_parley.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_parley.so
%{_desktopdir}/kde4/parley.desktop
%{_datadir}/apps/desktoptheme/default/widgets/parley_plasma_card.svg
%{_datadir}/apps/parley
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/config/*.knsrc
%{_iconsdir}/hicolor/*x*/apps/parley.png
%{_iconsdir}/hicolor/scalable/apps/parley*.svgz
%{_datadir}/kde4/services/plasma-dataengine-parley.desktop
%{_datadir}/kde4/services/plasma_parley.desktop
