%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname mate-text-editor

%define gi_major 1.0
%define girname  %mklibname %{name}-gir %{gi_major}

%bcond_without python

Summary:	Small but powerful text editor for MATE
Name:		pluma
Version:	1.26.0
Release:	2
License:	GPLv2+
Group:		Editors
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		fix-bin-sh.patch

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.13.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	yelp-tools
%if %{with python}
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
%endif

Requires:	caja-schemas
Requires:	glib2.0-common
Requires:	mate-desktop-schemas
Requires:	typelib(Peas)
Requires:	typelib(PeasGtk)
Requires:	zenity
%if %{with python}
Requires:	python
%endif

%rename		%{oname}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides Pluma, a small and lightweight UTF-8 text editor for
the MATE environment.

Pluma is part of MATE and uses the latest GTK+ and MATE libraries. Complete
MATE integration is featured, with support for Drag and Drop (DnD) from Caja
(the MATE file manager), the use of the MATE help system, the MATE Virtual
File System and the MATE print framework.

Pluma uses a Multiple Document Interface (MDI), which lets you edit more than
one document at the same time.

Pluma supports most standard editing features, plus several not found in your
average text editor (plugins being the most notable of these).

%files  -f %{name}.lang
%doc README* COPYING AUTHORS
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.spell.gschema.xml
%{_datadir}/metainfo/pluma.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.pythonconsole.gschema.xml
%{_datadir}/%{name}
%dir %{_libdir}/%{name}/plugins
#{_libdir}/%{name}/plugins/changecase.plugin
%{_libdir}/%{name}/plugins/docinfo.plugin
%{_libdir}/%{name}/plugins/filebrowser.plugin
%{_libdir}/%{name}/plugins/libtaglist.so
%{_libdir}/%{name}/plugins/modelines.plugin
%{_libdir}/%{name}/plugins/sort.plugin
%{_libdir}/%{name}/plugins/spell.plugin
%{_libdir}/%{name}/plugins/taglist.plugin
%{_libdir}/%{name}/plugins/time.plugin
#{_libdir}/%{name}/plugins/libchangecase.so
%{_libdir}/%{name}/plugins/libdocinfo.so
%{_libdir}/%{name}/plugins/libfilebrowser.so
%{_libdir}/%{name}/plugins/libmodelines.so
%{_libdir}/%{name}/plugins/libsort.so
%{_libdir}/%{name}/plugins/libspell.so
%{_libdir}/%{name}/plugins/libtime.so
%if %{with python}
%{_libdir}/%{name}/plugins/externaltools.plugin
%{_libdir}/%{name}/plugins/pythonconsole.plugin
%{_libdir}/%{name}/plugins/quickopen.plugin
%{_libdir}/%{name}/plugins/snippets.plugin
%{_libdir}/%{name}/plugins/externaltools
%{_libdir}/%{name}/plugins/pythonconsole
%{_libdir}/%{name}/plugins/quickopen
%{_libdir}/%{name}/plugins/snippets
%endif
%{_libdir}/%{name}/plugins/libtrailsave.so
%{_libdir}/%{name}/plugins/trailsave.plugin
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%package devel
Group:		Development/C
Summary:	Headers for writing Pluma plugins
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains includes files for developing plugins based on Pluma's
API.

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/pluma
%{_libdir}/pkgconfig/pluma.pc
%{_datadir}/gir-1.0/Pluma-%{gi_major}.gir

#---------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
#Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
This package contains GObject Introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Pluma-%{gi_major}.typelib

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
export PYTHON=%{__python}
%configure \
	--disable-schemas-compile \
        --enable-gtk-doc-html \
        --enable-gvfs-metadata \
%if %{with python}
	--enable-python \
%else
	--disable-python \
%endif
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

