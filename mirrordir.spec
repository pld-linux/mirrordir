Summary:	Easy to use directory mirroring tool
Summary(pl):	�atwy w u�yciu pakiet do mirrorowania katalog�w
Name:		mirrordir
Version:	0.10.49
Release:	0.1
Group:		Applications/Networking
License:	GPL
Source0:	http://mirrordir.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-datadir-fix.patch.bz2
Patch1:		%{name}-zlib-1.1.3-zfree.patch.bz2
URL:		http://mirrordir.sourceforge.net/
BuildRequires:	perl
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mirrordir mirrors filesystems over ftp or locally via a minimal set of
changes. It is optimised for locally mirroring a device as an
alternative to RAID devices. It duplicates file-systems in every
detail, even correctly recreating hardlinks, devices and access times.
It works well mirroring ftp sites that don't support ls-lR summaries.
Mirrordir can take a C script to customise the kind of files to mirror
based on their stat info, name, or other information.

Simply, use:
mirrordir ftp://some.where.com/dir /some/local/dir
or:
mirrordir /some/local/dir /other/local/directory

%description -l pl
Mirrordir wykonuje kopi� lokalnych system�w plik�w b�d� ftp. Jest
zoptymalizowany dla wykonywania lokalnych kopii dysk�w jako
alternatywa dla urz�dze� RAID. Kopiuje pliki z zachowaniem wszystkich
detali, w��cznie z czasami dost�pu do plik�w, odtwarzaj�c nawet
hardlinki. Sprawuje si� �wietnie przy wykonywaniu kopii katalog�w ftp
kt�re nie wspieraj� podsumowa� ls-lR. Mirror mo�e u�y� skryptu C do
wyszczeg�lnienia parametr�w mirrora.

Podsumowywuj�c, wpisz:
mirrordir ftp://gdzies.tam.pl/katalog /jakis/lokalny/katalog
lub:
mirrordir /jakis/loklany/katalog /inny/lokalny/katalog

%package libs
Summary:	mirrordir libraries
Summary(pl):	Biblioteki mirrordir
Group:		Libraries
Obsoletes:	libmirrordirz1
Obsoletes:	libdiffie1

%description libs
mirrordir libraries (mirrordirz and diffie), necessary to run
mirrordir.

%description libs -l pl
Biblioteki mirrordir (mirrordirz i diffie), potrzebne do dzia�ania
mirrordir.

%package devel
Summary:	mirrordir development package
Summary(pl):	Pakiet dla programist�w mirrordir
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Obsoletes:	libmirrordirz1-devel
Obsoletes:	libdiffie1-devel

%description devel
mirrordir development package - for programmers that use mirrordir
libraries.

%description devel -l pl
Pakiet programistyczny mirrordir - dla programist�w u�ywaj�cych
bibliotek mirrordir.

%package static
Summary:	mirrordir static libraries
Summary(pl):	Statyczne biblioteki mirrordir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of mirrordir libraries.

%description static -l pl
Statyczna wersja bibliotek mirrordir.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
perl -p -i -e 's/-f \$\(bindir\)\/mirrordir \$/-f \$\(bindir\)\/mirrordir \$\(DESTDIR\)\$/' src/Makefile

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libs -p /sbin/ldconfig
%postun	-n libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mirrordir
%config(noreplace) %{_sysconfdir}/secure*
%config(noreplace) %{_sysconfdir}/pam.d/*
%{_mandir}/man*/*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
