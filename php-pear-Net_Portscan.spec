%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Portscan
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Portscanner utilities
Summary(pl):	%{_class}_%{_subclass} - Narzêdzia skanuj±ce porty
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net_Portscan package allows one to perform basic portscanning
functions with PHP. It supports checking an individual port or
checking a whole range of ports on a machine.

%description -l pl
Pakiet Net_Portscan pozwala na podstawowe skany portów przy u¿yciu
PHP. Umo¿liwia sprawdzanie pojedyñczych portów, jak i ca³ych zakresów
portów na danej maszynie.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README*,tests/*}
%{php_pear_dir}/%{_class}/*.php
