%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname mate-text-editor

%bcond_without python

Summary:	Small but powerful text editor for MATE
Name:		pluma
Version:	1.18.2
Release:	1
License:	GPLv2+
Group:		Editors 
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	iso-codes
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
%if %{with python}
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pygtksourceview-2.0)
BuildRequires:	pkgconfig(python2)
%endif
Requires:	glib2.0-common
# the run-command plugin uses zenity
Requires:	pygtk2.0
Requires:	python-gtksourceview
Requires:	zenity
%rename %{oname}

%description
Pluma is a small but powerful text editor designed expressly
for MATE.

It includes such features as split-screen mode, a plugin
API, which allows Pluma to be extended to support many
features while remaining small at its core, multiple
document editing through the use of a 'tabbed' notebook and
many more functions.

%package devel
Group:		Development/C
Summary:	Headers for writing Pluma plugins
Provides:	%{name}-devel = %{version}-%{release}
%rename %{oname}-devel

%description devel
Pluma is a small but powerful text editor designed expressly
for MATE.

It includes such features as split-screen mode, a plugin
API, which allows Pluma to be extended to support many
features while remaining small at its core, multiple
document editing through the use of a 'tabbed' notebook and
many more functions.

Install this if you want to build plugins that use Pluma's API.

%prep
%setup -q
%apply_patches

%build
export PYTHON=%{__python2}
%configure \
        --enable-gtk-doc-html     \
	--enable-gvfs-metadata \
%if %{with python}
	--enable-python \
%else
	--disable-python \
%endif
	--disable-introspection \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%files  -f %{name}.lang
%doc README COPYING AUTHORS
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.spell.gschema.xml
%{_datadir}/appdata/pluma.appdata.xml
%{_datadir}/%{name}
#%dir %{_libdir}/%{name}/plugin-loaders
#%{_libdir}/%{name}/plugin-loaders/libcloader.so
#%{_libdir}/%{name}/plugin-loaders/libpythonloader.so
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/changecase.plugin
%{_libdir}/%{name}/plugins/docinfo.plugin
%{_libdir}/%{name}/plugins/filebrowser.plugin
%{_libdir}/%{name}/plugins/libtaglist.so
%{_libdir}/%{name}/plugins/modelines.plugin
%{_libdir}/%{name}/plugins/sort.plugin
%{_libdir}/%{name}/plugins/spell.plugin
%{_libdir}/%{name}/plugins/taglist.plugin
%{_libdir}/%{name}/plugins/time.plugin
%{_libdir}/%{name}/plugins/libchangecase.so
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

%files devel
%{_includedir}/pluma
%{_libdir}/pkgconfig/pluma.pc
%_datadir/gtk-doc/html/*

