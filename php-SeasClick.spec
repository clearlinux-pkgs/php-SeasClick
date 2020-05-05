#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-SeasClick
Version  : 0.1.0
Release  : 3
URL      : https://pecl.php.net//get/SeasClick-0.1.0.tgz
Source0  : https://pecl.php.net//get/SeasClick-0.1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: php-SeasClick-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-php

%description
SeasClick
=====
[![Build Status](https://travis-ci.org/SeasX/SeasClick.svg?branch=master)](https://travis-ci.org/SeasX/SeasClick)

%package lib
Summary: lib components for the php-SeasClick package.
Group: Libraries

%description lib
lib components for the php-SeasClick package.


%prep
%setup -q -n SeasClick-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/SeasClick.so
