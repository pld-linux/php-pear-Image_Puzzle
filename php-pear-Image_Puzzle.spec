%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Puzzle
%define		_status		beta
%define		_pearname	Image_Puzzle

Summary:	%{_pearname} - generates puzzle pieces from image file
Summary(pl.UTF-8):	%{_pearname} - generowanie części układanki na podstawie obrazka
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2f35d75d516b8e60af00137823ba3a5a
URL:		http://pear.php.net/package/Image_Puzzle/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Image_Color2 >= 0.1.0
Requires:	php-pear-PEAR >= 1:1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEAR::Image_Puzzle divides an image to puzzle pieces.
- Provides a few edge styles to generate puzzle pieces
- Allow saving each piece to separate files
- Allow getting information about each piece coordinates accoring to
  original image

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR::Image_Puzzle dzieli obrazek na części układanki:
- dostarcza kilka styli brzegów
- pozwala na zapisanie każdej części w osobnym pliku
- pozwala na uzyskanie informacji o współrzędnej każdej z części
  względem oryginalnego obrazka

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/Puzzle
%{php_pear_dir}/Image/Puzzle.php
