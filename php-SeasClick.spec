#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-SeasClick
Version  : 0.1.0
Release  : 8
URL      : https://pecl.php.net//get/SeasClick-0.1.0.tgz
Source0  : https://pecl.php.net//get/SeasClick-0.1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
BuildRequires : buildreq-cmake
BuildRequires : buildreq-php
Patch1: PHP-7.4-support.patch

%description
SeasClick
=====
[![Build Status](https://travis-ci.org/SeasX/SeasClick.svg?branch=master)](https://travis-ci.org/SeasX/SeasClick)

%prep
%setup -q -n SeasClick-0.1.0
cd %{_builddir}/SeasClick-0.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)
