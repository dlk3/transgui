%define  debug_package %{nil}

#  FPC source bundle: https://gitlab.com/freepascal.org/fpc/source/-/archive/56baf314b5ebf4e5a44fe3e214914fa2e1b34adb/source-56baf314b5ebf4e5a44fe3e214914fa2e1b34adb.tar.bz2

Name:		fpc
Version:	3.2.4
Release:	0%{?dist}
Summary:	Free Pascal Compiler
License:	GPLv2+ and LGPLv2+ with exceptions # https://wiki.lazarus.freepascal.org/FPC_modified_LGPL
URL:		https://www.freepascal.org
Source0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64

BuildRequires:	fpc == 3.2.2
BuildRequires: 	glibc-devel
BuildRequires:	qt5pas-devel
BuildRequires:  libX11-devel

%description
An updated, development version of the Free Pascal Compiler, intended only to
be used in the COPR build environment for building lighterowl's transgui 
package.  Do not install this on your workstation, it will break stuff.

%prep
%setup -q

%build
make all

%install
#make PREFIX=%{buildroot}/usr install
#mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
make install INSTALL_PREFIX=%{buildroot}/usr _LIB=%{_libdir}
install -m 644 -Dt %{buildroot}%{_sysconfdir}/profile.d fpc-path.sh

%files
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/libpas2jslib.so*
%{_sysconfdir}/profile.d/*
%dir %{_defaultdocdir}/%{name}-%{version}/
%doc %{_defaultdocdir}/%{name}-%{version}/*

%post
source %{_sysconfdir}/profile.d/fpc-path.sh
%{_libdir}/%{name}/%{version}/samplecfg %{_libdir}/%{name}/%version} %{_sysconfdir}
export

%changelog
* Sun Jun 08 2025 dlk3 <dave@daveking.com> 3.2.4-0
- Initial version of package
