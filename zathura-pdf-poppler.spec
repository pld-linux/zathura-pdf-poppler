Summary:	poppler based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF do zathury oparta na bibliotece poppler
Name:		zathura-pdf-poppler
Version:	0.3.0
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-poppler/download/%{name}-%{version}.tar.xz
# Source0-md5:	3d52abddb7b1a0cdd39689205c3cabed
URL:		https://pwmt.org/projects/zathura/zathura-pdf-poppler/
BuildRequires:	cairo-devel
# C11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	meson >= 0.43
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.18
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	zathura-devel >= 0.4.4
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	gtk+3 >= 3.2
Requires:	poppler-glib >= 0.18
Requires:	zathura >= 0.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

%description -l pl.UTF-8
Wtyczka zathura-pdf-poppler dodaje obsługę PDF do zathury przez użycie
silnika renderującego poppler.

%prep
%setup -q

%build
%meson build

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_libdir}/zathura/libpdf-poppler.so
%{_desktopdir}/org.pwmt.zathura-pdf-poppler.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-poppler.metainfo.xml
