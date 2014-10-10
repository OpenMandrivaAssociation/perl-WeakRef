%define module	WeakRef
%define name	perl-%{module}
%define version 0.01
%define release 11

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



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.01-10mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.01-9mdv2011.0
+ Revision: 555215
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.01-8mdv2010.0
+ Revision: 430655
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-7mdv2009.0
+ Revision: 258784
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-6mdv2009.0
+ Revision: 246699
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2008.1
+ Revision: 152393
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdv2008.0
+ Revision: 67090
- rebuild


* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2007.0
- Rebuild

* Wed Apr 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdk 
- first mandriva release

