%define  debug_package %{nil}

#  FPC source: https://gitlab.com/freepascal.org/fpc/source/-/archive/56baf314b5ebf4e5a44fe3e214914fa2e1b34adb/source-56baf314b5ebf4e5a44fe3e214914fa2e1b34adb.tar.bz2
%define fpc_commit 56baf314b5ebf4e5a44fe3e214914fa2e1b34adb

Name:		fpc
Version:	3.2.4
Release:	0%{dist}
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
make PREFIX=%{buildroot}/usr install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
mkdir %{buildroot}%{_sysconfigdir}
%{buildroot}/usr/lib64/%{name}/%{version}/samplecfg /usr/lib64/%{name}/%version} %{buildroot}%{_sysconfigdir}
install -m 644 -t %{buildroot}%{_sysconfigdir}/profile.d fpc-path.sh

%files
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/libpas2jslib.so*
%config(noreplace) %{_sysconfdir}/*
%dir %{_defaultdocdir}/%{name}-%{version}/
%doc %{_defaultdocdir}/%{name}-%{version}/*

%post
export PATH="%{_libdir}/%{name}/%{version}:$PATH
export

%changelog
* Sun Jun 08 2025 dlk3 <dave@daveking.com> 3.2.4-0
- Package creation
