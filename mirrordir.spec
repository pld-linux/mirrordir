
%define		_major1 1
%define		_libname1 libmirrordirz
%define		_major2 1
%define		_libname2 libdiffie

Name:		mirrordir
Summary:	Easy to use directory mirroring tool
Summary(pl):	£atwy w u¿yciu pakiet do mirrorowania katalogów
Version:	0.10.49
Release:	0.1
Source0:	http://mirrordir.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-datadir-fix.patch.bz2
Patch1:		%{name}-zlib-1.1.3-zfree.patch.bz2
Group:		Applications/Networking
URL:		http://mirrordir.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL
Requires:	%{_libname1}%{_major1} = %{version}
Requires:	%{_libname2}%{_major2} = %{version}

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
Mirrordir wykonuje kopiê lokalnych systemów plików b±d¼ ftp. Jest
zoptymalizowany dla wykonywania lokalnych kopii dysków jako
alternatywa dla urz±dzeñ RAID. Kopiuje pliki z zachowaniem wszystkich
detali, w³±cznie z czasami dostêpu do plików, odtwarzaj±c nawet
hadrdlinki. Sprawuje siê ¶wietnie przy wykonywaniu kopii katalogów ftp
które nie wspieraj± podsumowañ ls-lR. Mirror mo¿e u¿yæ skryptu C do
wyszczególnienia parametrów mirrora.

Podsumowywuj±c, wpisz:
mirrordir ftp://gdzies.tam.pl/katalog /jakis/lokalny/katalog
lub:
mirrordir /jakis/loklany/katalog /inny/lokalny/katalog

%package -n %{_libname1}%{_major1}
Summary:	The mirrordirz library, necessary to run mirrordir
Summary(pl):	Biblioteka mirrordirz, niezbêdna do uruchomienia mirrordir
Group:		Development/Libraries

%description -n %{_libname1}%{_major1}
The mirrordirz library, necessary to run mirrordir.

%description -n %{_libname1}%{_major1} -l pl
Biblioteka mirrordirz, niezbêdna do uruchomienia mirrordir.

%package -n %{_libname1}%{_major1}-devel
Summary:	Static version of the mirrordirz library
Summary(pl):	Statyczna wersja biblioteki mirrordirz
Group:		Development/Libraries
Requires:	%{_libname1}%{_major1} = %{version}
Provides:	%{_libname1}-devel

%description -n %{_libname1}%{_major1}-devel
Static version of the mirrordirz library.

%description -n %{_libname1}%{_major1}-devel -l pl
Statyczna wersja biblioteki mirrordirz.

%package -n %{_libname2}%{_major2}
Summary:	The diffie library, necessary to run mirrordir
Summary(pl):	Biblioteka diffie, niezbêdna do uruchomienia mirrordir
Group:		Development/Libraries

%description -n %{_libname2}%{_major2}
The diffie library, necessary to run mirrordir.

%description -n %{_libname2}%{_major2} -l pl
Biblioteka diffie, niezbêdna do uruchomienia mirrordir

%package -n %{_libname2}%{_major2}-devel
Summary:	Static version of the diffie library
Summary(pl):	Statyczna wersja biblioteki diffie
Group:		Development/Libraries
Requires:	%{_libname2}%{_major2} = %{version}
Provides:	%{_libname2}-devel

%description -n %{_libname2}%{_major2}-devel
Static version of the diffie library.

%description -n %{_libname2}%{_major2}-devel -l pl
Statyczna wersja biblioteki diffie.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p1
%patch1 -p1 -b .zfree

%build
%configure2_13
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
perl -p -i -e 's/-f \$\(bindir\)\/mirrordir \$/-f \$\(bindir\)\/mirrordir \$\(DESTDIR\)\$/' src/Makefile
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%post -n %{_libname1}%{_major1} -p /sbin/ldconfig

%postun -n %{_libname1}%{_major1} -p /sbin/ldconfig

%post -n %{_libname2}%{_major2} -p /sbin/ldconfig

%postun -n %{_libname2}%{_major2} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mirrordir
%config(noreplace) %{_sysconfdir}/secure*
%config(noreplace) %{_sysconfdir}/pam.d/*
%{_mandir}/man*/*

%files -n %{_libname1}%{_major1}
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%{_libdir}/%{_libname1}.so.*

%files -n %{_libname1}%{_major1}-devel
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%{_libdir}/%{_libname1}.so
%{_libdir}/%{_libname1}.a
%{_libdir}/%{_libname1}.la

%files -n %{_libname2}%{_major2}
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%{_libdir}/%{_libname2}.so.*

%files -n %{_libname2}%{_major2}-devel
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS THANKS TODO
%{_libdir}/%{_libname2}.so
%{_libdir}/%{_libname2}.a
%{_libdir}/%{_libname2}.la
