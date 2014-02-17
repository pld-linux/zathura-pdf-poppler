Summary:	poppler based PDF plugin for zathura
Name:		zathura-pdf-poppler
Version:	0.2.5
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.gz
# Source0-md5:	e314b8b136e71aa4925a864141f12d15
URL:		http://pwmt.org/projects/zathura/plugins/zathura-pdf-poppler
BuildRequires:	cairo-devel
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	zathura-devel >= 0.2.0
Requires:	zathura >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/zathura/pdf.so
%{_desktopdir}/%{name}.desktop
