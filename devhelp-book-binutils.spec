Summary:	DevHelp book: binutils
Summary(pl):	Ksi±¿ka do DevHelp'a o binutils
Name:		devhelp-book-binutils
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/binutils.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about binutils

%description -l pl
Ksi±¿ka do DevHelp o binutils

%prep
%setup -q -c binutils -n binutils

%build
mv -f book binutils
mv -f book.devhelp binutils.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/binutils-2.10.1
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install binutils.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install binutils/* $RPM_BUILD_ROOT%{_prefix}/books/binutils-2.10.1

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
