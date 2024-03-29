Summary:	Easy to use directory mirroring tool
Summary(pl.UTF-8):	Łatwy w użyciu pakiet do mirrorowania katalogów
Name:		mirrordir
Version:	0.10.49
Release:	1
Group:		Applications/Networking
License:	GPL
Source0:	http://mirrordir.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	7671e541b5971ad863bba811ac77f69e
Patch0:		%{name}-datadir-fix.patch
Patch1:		%{name}-zlib-1.1.3-zfree.patch
URL:		http://mirrordir.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-base
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mirrordir mirrors filesystems over FTP or locally via a minimal set of
changes. It is optimised for locally mirroring a device as an
alternative to RAID devices. It duplicates file-systems in every
detail, even correctly recreating hardlinks, devices and access times.
It works well mirroring FTP sites that don't support ls-lR summaries.
Mirrordir can take a C script to customise the kind of files to mirror
based on their stat info, name, or other information.

Simply, use:
mirrordir ftp://some.where.com/dir /some/local/dir
or:
mirrordir /some/local/dir /other/local/directory

%description -l pl.UTF-8
Mirrordir wykonuje kopię lokalnych systemów plików bądź FTP. Jest
zoptymalizowany dla wykonywania lokalnych kopii dysków jako alternatywa 
dla urządzeń RAID. Kopiuje pliki z zachowaniem wszystkich detali, 
włącznie z czasami dostępu do plików, odtwarzając nawet hardlinki. 
Sprawuje się świetnie przy wykonywaniu kopii katalogów FTP które nie 
wspierają podsumowań ls-lR. Mirror może użyć skryptu C do 
wyszczególnienia parametrów mirrora.

Podsumowując, wpisz:
mirrordir ftp://gdzies.tam.pl/katalog /jakis/lokalny/katalog
lub:
mirrordir /jakis/loklany/katalog /inny/lokalny/katalog

%package libs
Summary:	mirrordir libraries
Summary(pl.UTF-8):	Biblioteki mirrordir
Group:		Libraries
Obsoletes:	libmirrordirz1
Obsoletes:	libdiffie1

%description libs
mirrordir libraries (mirrordirz and diffie), necessary to run
mirrordir.

%description libs -l pl.UTF-8
Biblioteki mirrordir (mirrordirz i diffie), potrzebne do działania
mirrordir.

%package devel
Summary:	mirrordir development package
Summary(pl.UTF-8):	Pakiet dla programistów mirrordir
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libmirrordirz1-devel
Obsoletes:	libdiffie1-devel

%description devel
mirrordir development package - for programmers that use mirrordir
libraries.

%description devel -l pl.UTF-8
Pakiet programistyczny mirrordir - dla programistów używających
bibliotek mirrordir.

%package static
Summary:	mirrordir static libraries
Summary(pl.UTF-8):	Statyczne biblioteki mirrordir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of mirrordir libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek mirrordir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__perl} -pi -e 's/-f \$\(bindir\)\/mirrordir \$/-f \$\(bindir\)\/mirrordir \$\(DESTDIR\)\$/' src/Makefile

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mirrordir
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/secure*
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*
%{_mandir}/man*/*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
