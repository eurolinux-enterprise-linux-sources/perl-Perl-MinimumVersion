Name:           perl-Perl-MinimumVersion
Version:        1.32
Release:        1%{?dist}
Summary:        Find a minimum required version of perl for Perl code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-MinimumVersion/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Perl-MinimumVersion-%{version}.tar.gz

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires: perl(Cwd)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.59
# Run-time and tests:
BuildRequires: perl(List::Util) >= 1.20
BuildRequires: perl(Params::Util) >= 0.25
BuildRequires: perl(Perl::Critic::Utils) >= 1.104
BuildRequires: perl(PPI) >= 1.215
BuildRequires: perl(PPIx::Regexp) >= 0.029
BuildRequires: perl(version) >= 0.76
%if !%{defined perl_bootstrap}
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Find::Rule) >= 0.32
BuildRequires: perl(File::Find::Rule::Perl) >= 1.04
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(PPI::Util)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Script) >= 1.03
%endif

%description
Find a minimum required version of perl for Perl code

%prep
%setup -q -n Perl-MinimumVersion-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
make test
%endif

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{_bindir}/*
%{perl_vendorlib}/Perl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jan 18 2013 Ralf Corsépius - 1.32-1
- Upstream update.
- Add BR: perl(PPIx::Regexp).
- Reflect upstream URL having changed.

* Wed Oct 24 2012 Petr Pisar <ppisar@redhat.com> - 1.28-8
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.28-6
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.28-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.28-3
- Perl mass rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.28-2
- use perl_bootstrap macro

* Fri Jun 17 2011 Ralf Corsépius <ralf.corsepius@fedoraproject.org> - 1.28-1
- Upstream update.
- Remove maintainer test (Upstream doesn't want us to find his bugs).
- Update BR's.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.26-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Aug 05 2010 Ralf Corsépius <ralf.corsepius@fedoraproject.org> - 1.26-1
- Upstream update.
 
* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.24-3
- Mass rebuild with perl-5.12.0

* Mon May  3 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.24-2
- for the meantime apply changes from trunk. Other builds using
 this package should succed with perl-5.12.

* Mon Mar 01 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.24-1
- Upstream update.
- Adjust BR's.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.20-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.20-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.19-1
- Upstream update.

* Mon Aug 25 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.18-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.15-5
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-4
- correct List::Util version, perl 5.10.0 has 1.19

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-3
- rebuild for new perl

* Thu Jan 10 2008 Ralf Corsépius <rc040203@freenet.de> - 0.15.2
- Use unversioned BR: perl(version) to circumvent perl vs. rpm versioning 
  conflicts

* Tue Nov 20 2007 Ralf Corsépius <rc040203@freenet.de> - 0.15-1
- Initial version.
