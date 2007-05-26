Summary:	Easily extensible archive format
Name:		xar
Version:	1.5
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://xar.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8057051827329458c111a4880e868afc
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

%package devel
Summary:	Header files and develpment documentation for xar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for xar.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/xar
