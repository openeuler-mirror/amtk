Name:           amtk
Version:        5.0.0
Release:        3
Summary:        Actions, Menus and Toolbars Kit for GTK+ applications
License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Amtk
Source0:        https://download.gnome.org/sources/amtk/5.0/amtk-%{version}.tar.xz

BuildRequires:  gcc gettext glib2-devel gobject-introspection-devel gtk3-devel

%description
Amtk is the acronym for “Actions, Menus and Toolbars Kit”. It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

%package        devel
Summary:        Header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

Provides:       %{name}-tests = %{version}-%{release}
Obsoletes:      %{name}-tests < %{version}-%{release}

%description    devel
Header files for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --enable-installed-tests
%make_build V=1

%install
%make_install
%delete_la

%find_lang amtk-5

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Amtk-5.typelib
%{_libdir}/libamtk-5.so.0*
%{_datadir}/locale/*

%files devel
%defattr(-,root,root)
%{_includedir}/amtk-5/
%{_libdir}/libamtk-5.so
%{_libdir}/pkgconfig/amtk-5.pc
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/amtk-5/

%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Amtk-5.gir
%dir %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/html/amtk-5.0/
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/amtk-5/

%changelog
* Wed Dec 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.0.0-3
- Package init
