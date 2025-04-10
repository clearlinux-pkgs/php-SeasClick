#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : php-SeasClick
Version  : 0.1.1
Release  : 71
URL      : https://github.com/SeasX/SeasClick/archive/refs/tags/SeasClick-0.1.1.zip
Source0  : https://github.com/SeasX/SeasClick/archive/refs/tags/SeasClick-0.1.1.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause MIT
Requires: php-SeasClick-lib = %{version}-%{release}
Requires: php-SeasClick-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SeasClick
=====
[![Build Status](https://travis-ci.org/SeasX/SeasClick.svg?branch=master)](https://travis-ci.org/SeasX/SeasClick)

%package lib
Summary: lib components for the php-SeasClick package.
Group: Libraries
Requires: php-SeasClick-license = %{version}-%{release}

%description lib
lib components for the php-SeasClick package.


%package license
Summary: license components for the php-SeasClick package.
Group: Default

%description license
license components for the php-SeasClick package.


%prep
%setup -q -n SeasClick-SeasClick-0.1.1
cd %{_builddir}/SeasClick-SeasClick-0.1.1
pushd ..
cp -a SeasClick-SeasClick-0.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-SeasClick
cp %{_builddir}/SeasClick-SeasClick-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-SeasClick/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/SeasClick-SeasClick-%{version}/lib/clickhouse-cpp/LICENSE %{buildroot}/usr/share/package-licenses/php-SeasClick/7c8514020b31188942eff850b971ab46e3f1374e || :
cp %{_builddir}/SeasClick-SeasClick-%{version}/lib/clickhouse-cpp/contrib/cityhash/COPYING %{buildroot}/usr/share/package-licenses/php-SeasClick/5b9b98c0857d4c15cd80f482063807c1dec9ed8a || :
cp %{_builddir}/SeasClick-SeasClick-%{version}/lib/clickhouse-cpp/contrib/lz4/LICENSE %{buildroot}/usr/share/package-licenses/php-SeasClick/e05fb60a683ec949fb82bd5d1e70f0523549895a || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20240924/SeasClick.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-SeasClick/5b9b98c0857d4c15cd80f482063807c1dec9ed8a
/usr/share/package-licenses/php-SeasClick/7c8514020b31188942eff850b971ab46e3f1374e
/usr/share/package-licenses/php-SeasClick/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/php-SeasClick/e05fb60a683ec949fb82bd5d1e70f0523549895a
