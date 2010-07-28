%define upstream_name    MooseX-Clone
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    The L<Moose::Meta::Attribute>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Visitor)
BuildRequires: perl(Hash::Util::FieldHash::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(namespace::clean)
Provides: perl(MooseX::Clone::Meta::Attribute::Trait::StorableClone)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Out of the box the Moose manpage only provides very barebones cloning
support in order to maximize flexibility.

This role provides a 'clone' method that makes use of the low level cloning
support already in the Moose manpage and adds selective deep cloning based
on introspection on top of that. Attributes with the 'Clone' trait will
handle cloning of data within the object, typically delegating to the
attribute value's own 'clone' method.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


