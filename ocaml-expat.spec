%define name	ocaml-expat
%define version	0.9.1
%define release	%mkrel 9

Name:		ocaml-expat
Version:	0.9.1
Release:	10
Summary:	Ocaml wrapper for the Expat XML parsing library
License:	GPL
Group:		Development/Other
URL:		http://www.xs4all.nl/~mmzeeman/ocaml
Source0: 	http://www.xs4all.nl/~mmzeeman/ocaml/%{name}-%{version}.tar.bz2
BuildRequires:	ocaml
BuildRequires:  ocaml-findlib
BuildRequires:	expat-devel

%description
An ocaml wrapper for the Expat XML parsing library. It allows you to write
XML-Parsers using the SAX method. An XML document is parsed on the fly without
needing to load the entire XML-Tree into memory.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	expat-devel
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q

%build
%make depend
%make all allopt

%install
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_DESTDIR="%{buildroot}%{_libdir}/ocaml"
rm -f %{buildroot}/%{_libdir}/ocaml/stublibs/*.owner

%files
%doc LICENCE README doc
%dir %{_libdir}/ocaml/expat
%{_libdir}/ocaml/expat/*.cmi
%{_libdir}/ocaml/expat/*.cma
%{_libdir}/ocaml/expat/META
%{_libdir}/ocaml/stublibs/*.so

%files devel
%{_libdir}/ocaml/expat/*.a
%{_libdir}/ocaml/expat/*.cmxa
%{_libdir}/ocaml/expat/*.mli


%changelog
* Wed Nov 02 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.1-10
+ Revision: 712298
- rebuild against new ocaml version
- cleanup

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-9mdv2011.0
+ Revision: 389828
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-8mdv2009.1
+ Revision: 320722
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-5mdv2008.1
+ Revision: 178367
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-4mdv2008.0
+ Revision: 77677
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Sat Jun 23 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.1-3mdv2008.0
+ Revision: 43341
- build 'allopt' too

* Tue Jun 19 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.1-2mdv2008.0
+ Revision: 41240
- rebuild against new ocaml

* Thu Apr 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 18421
- Import ocaml-expat



* Thu Apr 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-1mdv2008.0
- first mdv release
