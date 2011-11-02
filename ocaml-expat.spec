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
