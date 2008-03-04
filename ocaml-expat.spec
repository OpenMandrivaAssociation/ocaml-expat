%define name	ocaml-expat
%define version	0.9.1
%define release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Ocaml wrapper for the Expat XML parsing library
License:	GPL
Group:		Development/Other
URL:		http://www.xs4all.nl/~mmzeeman/ocaml
Source0: 	http://www.xs4all.nl/~mmzeeman/ocaml/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-destdir.patch
BuildRequires:	ocaml
BuildRequires:	expat-devel
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{name}-%{version}
%patch

%build
%make depend
%make all allopt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE README doc
%dir %{ocaml_sitelib}/expat
%{ocaml_sitelib}/expat/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/expat/*
%exclude %{ocaml_sitelib}/expat/*.cmi
%{ocaml_sitelib}/stublibs/dllmlexpat.so
