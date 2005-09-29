%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Portscan
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - portscanner utilities
Summary(pl):	%{_pearname} - narz�dzia skanuj�ce porty
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	2.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	37f71b85c3f9a4acff42d019b6d23cd3
URL:		http://pear.php.net/package/Net_Portscan/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net_Portscan package allows one to perform basic portscanning
functions with PHP. It supports checking an individual port or
checking a whole range of ports on a machine.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet Net_Portscan pozwala na podstawowe skany port�w przy u�yciu
PHP. Umo�liwia sprawdzanie pojedynczych port�w, jak i ca�ych zakres�w
port�w na danej maszynie.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/tests/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
