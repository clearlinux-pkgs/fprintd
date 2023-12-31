#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : fprintd
Version  : 1.94.2
Release  : 5
URL      : https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v1.94.2/fprintd-v1.94.2.tar.gz
Source0  : https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v1.94.2/fprintd-v1.94.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: fprintd-bin = %{version}-%{release}
Requires: fprintd-data = %{version}-%{release}
Requires: fprintd-lib = %{version}-%{release}
Requires: fprintd-libexec = %{version}-%{release}
Requires: fprintd-license = %{version}-%{release}
Requires: fprintd-locales = %{version}-%{release}
Requires: fprintd-man = %{version}-%{release}
Requires: fprintd-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : dbus-python-python3
BuildRequires : glib-dev
BuildRequires : gobject-introspection
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pam_wrapper
BuildRequires : pam_wrapper-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libfprint-2)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : polkit-dev
BuildRequires : pypi(gi)
BuildRequires : pypi(pycairo)
BuildRequires : pypi-python_dbusmock-python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: notest.patch

%description
fprintd
=======
https://fprint.freedesktop.org/
Daemon to offer libfprint functionality over D-Bus
Might eat your kangaroo.

%package bin
Summary: bin components for the fprintd package.
Group: Binaries
Requires: fprintd-data = %{version}-%{release}
Requires: fprintd-libexec = %{version}-%{release}
Requires: fprintd-license = %{version}-%{release}
Requires: fprintd-services = %{version}-%{release}

%description bin
bin components for the fprintd package.


%package data
Summary: data components for the fprintd package.
Group: Data

%description data
data components for the fprintd package.


%package lib
Summary: lib components for the fprintd package.
Group: Libraries
Requires: fprintd-data = %{version}-%{release}
Requires: fprintd-libexec = %{version}-%{release}
Requires: fprintd-license = %{version}-%{release}

%description lib
lib components for the fprintd package.


%package libexec
Summary: libexec components for the fprintd package.
Group: Default
Requires: fprintd-license = %{version}-%{release}

%description libexec
libexec components for the fprintd package.


%package license
Summary: license components for the fprintd package.
Group: Default

%description license
license components for the fprintd package.


%package locales
Summary: locales components for the fprintd package.
Group: Default

%description locales
locales components for the fprintd package.


%package man
Summary: man components for the fprintd package.
Group: Default

%description man
man components for the fprintd package.


%package services
Summary: services components for the fprintd package.
Group: Systemd services
Requires: systemd

%description services
services components for the fprintd package.


%prep
%setup -q -n fprintd-v1.94.2
cd %{_builddir}/fprintd-v1.94.2
%patch -P 1 -p1
pushd ..
cp -a fprintd-v1.94.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687448817
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/fprintd
cp %{_builddir}/fprintd-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/fprintd/5821ee1deba963c8e12c6af89224de0d0d47bb53 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang fprintd
## install_append content
mv %{buildroot}/lib64 %{buildroot}/usr
mv %{buildroot}-v3/lib64 %{buildroot}-v3/usr
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/fprintd-delete
/V3/usr/bin/fprintd-enroll
/V3/usr/bin/fprintd-list
/V3/usr/bin/fprintd-verify
/usr/bin/fprintd-delete
/usr/bin/fprintd-enroll
/usr/bin/fprintd-list
/usr/bin/fprintd-verify

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
/usr/share/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml
/usr/share/dbus-1/system-services/net.reactivated.Fprint.service
/usr/share/dbus-1/system.d/net.reactivated.Fprint.conf
/usr/share/polkit-1/actions/net.reactivated.fprint.device.policy

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/security/pam_fprintd.so
/usr/lib64/security/pam_fprintd.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/fprintd
/usr/libexec/fprintd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fprintd/5821ee1deba963c8e12c6af89224de0d0d47bb53

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fprintd.1
/usr/share/man/man8/pam_fprintd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fprintd.service

%files locales -f fprintd.lang
%defattr(-,root,root,-)

