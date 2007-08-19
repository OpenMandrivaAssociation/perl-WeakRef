%define module	WeakRef
%define name	perl-%{module}
%define version 0.01
%define release %mkrel 3

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    An API to the Perl weak references
License:	    GPL or Artistic
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/WeakRef/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
A patch to Perl 5.005_55 by the author implements a core API for weak
references. This module is a Perl-level interface to that API, allowing weak
references to be created in Perl.

A weak reference is just like an ordinary Perl reference except that it isn't
included in the reference count of the thing referred to. This means that once
all references to a particular piece of data are weak, the piece of data is
freed and all the weak references are set to undef. This is particularly useful
for implementing circular data structures without memory leaks or caches of
objects.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/*/*

