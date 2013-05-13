Summary:	poppler based PDF plugin for zathura
Name:		zathura-pdf-poppler
Version:	0.2.3
Release:	1
License:	BSD-like
Group:		Applications
Source0:	https://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.gz
# Source0-md5:	1d8deb2d2ee5a6847267f977b8f2e542
URL:		http://pwmt.org/projects/zathura/plugins/zathura-pdf-poppler
BuildRequires:	girara-devel
BuildRequires:	gtk+2-devel >= 2:2.18.6
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	zathura-devel
Requires:	zathura >= 0.1.0
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
