%define url_ver %(echo %{version}|cut -d. -f1,2)
%define build_with_python 1
%define oname mate-text-editor

Summary:       Small but powerful text editor for MATE
Name:          pluma
Version:       1.6.0
Release:       2
License:       GPLv2+
Group:         Editors 
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires: aspell-devel
BuildRequires: enchant-devel
BuildRequires: iso-codes
BuildRequires: docbook-dtd412-xml
BuildRequires: intltool
BuildRequires: xml2po
BuildRequires: mate-common
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(enchant)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(gtksourceview-2.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
%if %{build_with_python}
BuildRequires: pkgconfig(pygobject-2.0)
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: pkgconfig(pygtksourceview-2.0)
BuildRequires: python
%endif

Requires:      pyorbit
# the run-command plugin uses zenity
Requires:      zenity

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
Group:    Development/C
Summary:  Headers for writing Pluma plugins
Provides: %{name}-devel = %{version}-%{release}
Provides: %{oname}-devel = %{version}-%{release}

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
%setup -q -n %{oname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
        --enable-gtk-doc     \
        --enable-gvfs-metadata    \
%if %{build_with_python}
        --enable-python 
%else
        --disable-python
%endif

%make LIBS='-lm -lgmodule-2.0'

%install

%makeinstall_std

%{find_lang} %{name} --with-gnome

%files  -f %{name}.lang
%doc README COPYING AUTHORS
%{_bindir}/pluma
%{_bindir}/mate-text-editor
%{_datadir}/pluma
%{_datadir}/mate/help/pluma
%{_datadir}/applications/pluma.desktop
%{_mandir}/man1/*
%{_libexecdir}/pluma
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/MateConf/gsettings/pluma.convert

%files devel
%{_includedir}/pluma
%{_libdir}/pkgconfig/pluma.pc
%_datadir/gtk-doc/html/*


