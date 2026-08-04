Name:		ocaml-expat
Version:	1.3.0
Release:	4
Summary:	OCaml wrapper for the Expat XML parsing library
License:	MIT
Group:		Development/Other
URL:		https://github.com/whitequark/ocaml-expat
Source0:	https://github.com/whitequark/ocaml-expat/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
BuildRequires:	pkgconfig(expat)

%description
An ocaml wrapper for the Expat XML parsing library. It allows you to write
XML-Parsers using the SAX method. An XML document is parsed on the fly without
needing to load the entire XML-Tree into memory.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	pkgconfig(expat)
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%autosetup
# Use system include/lib paths and package CFLAGS
sed -e 's|-O2 -I\$(EXPAT_INCDIR)|%{optflags}|' \
	-e 's|EXPAT_LIBDIR=/usr/local/lib|EXPAT_LIBDIR=%{_libdir}|' \
	-e 's|EXPAT_INCDIR=/usr/local/include|EXPAT_INCDIR=%{_includedir}|' \
	-e 's/\$(OCAMLMKLIB)/& -g/' \
	-i Makefile

%build
%make_build depend
%make_build -j1 all allopt \
	OCAMLC="ocamlc -g" \
	OCAMLOPT="ocamlopt -g"

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
rm -f %{buildroot}%{_libdir}/ocaml/stublibs/*.owner

%files
%doc README changelog
%license LICENCE
%dir %{_libdir}/ocaml/expat
%{_libdir}/ocaml/expat/*.cmi
%{_libdir}/ocaml/expat/*.cma
%{_libdir}/ocaml/expat/META
%{_libdir}/ocaml/stublibs/*.so

%files devel
%{_libdir}/ocaml/expat/*.a
%{_libdir}/ocaml/expat/*.cmxa
%{_libdir}/ocaml/expat/*.cmxs
%{_libdir}/ocaml/expat/*.mli
