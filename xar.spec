Summary:	Easily extensible archive format
Summary(pl.UTF-8):	Łatwo rozszerzalny format archiwów
Name:		xar
Version:	1.5.2
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://xar.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8eabb055d3387b8edc30ecfb08d2e80d
URL:		http://code.google.com/p/xar/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
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
Summary:	Header files for xar
Summary(pl.UTF-8):	Pliki nagłówkowe xara
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for xar.

%description devel -l pl.UTF-8
Pliki nagłówkowe xara.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{*.a,*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/xar
%attr(755,root,root) %{_libdir}/libxar.so.*
%{_mandir}/man1/xar.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxar.so
%dir %{_includedir}/xar
%{_includedir}/xar/xar.h
