Summary:	DevHelp book: binutils
Summary(pl.UTF-8):	Książka do DevHelpa o binutils
Name:		devhelp-book-binutils
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/binutils.tar.gz
# Source0-md5:	40ab60cd6e72ac35086c791cfd6ae4da
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about binutils.

%description -l pl.UTF-8
Książka do DevHelpa o binutils.

%prep
%setup -q -c -n binutils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/binutils-2.10.1

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/binutils-2.10.1/binutils-2.10.1.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/binutils-2.10.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
