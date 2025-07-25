%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura 2> /dev/null || echo -1)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura 2> /dev/null || echo -1)

Summary:	poppler based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF do zathury oparta na bibliotece poppler
Name:		zathura-pdf-poppler
Version:	0.3.3
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-poppler/download/%{name}-%{version}.tar.xz
# Source0-md5:	732930b4e945357e472ed542cad62284
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
Requires:	zathura(plugin-abi) = %_zathura_abi_ver
Requires:	zathura(plugin-api) = %_zathura_api_ver
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
