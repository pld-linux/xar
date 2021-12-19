Summary:	Easily extensible archive format
Summary(pl.UTF-8):	Łatwo rozszerzalny format archiwów
Name:		xar
Version:	1.6.1
Release:	2
License:	BSD
Group:		Applications/Archiving
Source0:	https://github.com/downloads/mackyle/xar/%{name}-%{version}.tar.gz
# Source0-md5:	a624535d6a1e8fdf420b36a6b334047b
Patch0:		build.patch
URL:		https://mackyle.github.io/xar/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	libxml2-devel >= 1:2.6.11
BuildRequires:	openssl-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	libxml2 >= 1:2.6.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XAR project aims to provide an easily extensible archive format.
Important design decisions include an easily extensible XML table of
contents for random access to archived files, storing the toc at the
beginning of the archive to allow for efficient handling of streamed
archives, the ability to handle files of arbitrarily large sizes, the
ability to choose independent encodings for individual files in the
archive, the ability to store checksums for individual files in both
compressed and uncompressed form, and the ability to query the table
of content's rich meta-data.

%description -l pl.UTF-8
Celem projektu XAR jest zapewnienie łatwo rozszerzalnego formatu
archiwów. Główne decyzje projektowe obejmują: łatwo rozszerzalną
tabelę zawartości w formacie XML do swobodnego dostępu do
zarchiwizowanych plików, zapisywanie informacji o zawartości archiwum
na początku archiwum w celu umożliwienia wydajnej obsługi archiwów
strumieniowych, możliwość obsługi plików o dowolnie dużych rozmiarach,
możliwość wyboru niezależnych kodowań dla poszczególnych plików w
archiwum, możliwość zapisywania sum kontrolnych dla poszczególnych
plików w zarówno skompresowanej jak i nieskompresowanej postaci,
możliwość odpytywania metadanych tabeli zawartości.

%package devel
Summary:	Header files for xar library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xara
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	acl-devel
Requires:	bzip2-devel
Requires:	libxml2-devel >= 1:2.6.11
Requires:	openssl-devel
Requires:	xz-devel
Requires:	zlib-devel

%description devel
Header files for xar library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xara.

%package static
Summary:	Static xar library
Summary(pl.UTF-8):	Statyczna biblioteka xara
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xar library.

%description static -l pl.UTF-8
Statyczna biblioteka xara.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS xar_README.txt ChangeLog
%attr(755,root,root) %{_bindir}/xar
%attr(755,root,root) %{_libdir}/libxar.so.1
%{_mandir}/man1/xar.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxar.so
%{_libdir}/libxar.la
%dir %{_includedir}/xar
%{_includedir}/xar/xar.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxar.a
