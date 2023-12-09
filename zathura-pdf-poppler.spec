Summary:	poppler based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF do zathury oparta na bibliotece poppler
Name:		zathura-pdf-poppler
Version:	0.3.2
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-poppler/download/%{name}-%{version}.tar.xz
# Source0-md5:	d91018be0282c09a1e84d83b9fdc08b9
URL:		https://pwmt.org/projects/zathura/zathura-pdf-poppler/
BuildRequires:	cairo-devel
# C17
BuildRequires:	gcc >= 6:8.1
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	meson >= 0.61
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 21.12
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.5.3
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	gtk+3 >= 3.2
Requires:	poppler-glib >= 21.12
Requires:	zathura >= 0.5.3
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

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/zathura/libpdf-poppler.so
%{_desktopdir}/org.pwmt.zathura-pdf-poppler.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-poppler.metainfo.xml
