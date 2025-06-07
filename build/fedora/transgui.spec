%define  debug_package %{nil}

Name:		transgui
Version:	5.18.7.f
Release:	1%{?dist}
Summary:	Transmission BitTorrent client

License:	GPLv2
URL:		https://github.com/lighterowl/transgui
Source0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64

Requires: GeoIP
Requires: GeoIP-GeoLite-data   

BuildRequires:	lazarus
BuildRequires:	fpc
BuildRequires:  openssl-devel
BuildRequires:  dbus-devel

%description
Transmission Remote GUI is feature rich cross platform front-end to remotely
control Transmission daemon via its RPC protocol. It is faster and has more
functionality than builtin Transmission web interface.

%prep
%setup -q

%build
lazbuild transgui.lpi

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} units/transgui
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 -t %{buildroot}%{_datadir}/applications transgui.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 -t %{buildroot}%{_datadir}/icons/hicolor/48x48/apps transgui.png
mkdir -p %{buildroot}%{_datadir}/transgui/lang
install -m 644 -t %{buildroot}%{_datadir}/transgui/lang lang/transgui.*

%files
%license LICENSE
%doc README.md
%{_bindir}/transgui
%{_datadir}/applications/transgui.desktop
%{_datadir}/icons/hicolor/48x48/apps/transgui.png
%{_datadir}/transgui/lang

%changelog
* Fri Jun 6 2025 David King <dave@daveking.com> - 5.18.8.f-1
	Changed build process to use fpc-3.2.4 and lazarus-4.0.0
* Fri May 30 2025 David King <dave@daveking.com> - 5.18.8.f-0
	Migrated to the lighterowl fork to fix issue restoring window size on restart
* Sun Sep 10 2023 David King <dave@daveking.com> - 5.18.0-3
	Updated to latest development code from github.com
* Wed Nov 16 2022 David King <dave@daveking.com> - 5.18.0-2
	Fixes to support Transmission 3.0
* Sat Dec 14 2019 David King <dave@daveking.com> - 5.18.0-1
	Initial Version
