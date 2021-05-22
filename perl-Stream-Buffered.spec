#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Stream-Buffered
Version  : 0.03
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOY/Stream-Buffered-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOY/Stream-Buffered-0.03.tar.gz
Summary  : 'temporary buffer to save bytes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Stream-Buffered-license = %{version}-%{release}
Requires: perl-Stream-Buffered-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Stream::Buffered - temporary buffer to save bytes
SYNOPSIS
my $buf = Stream::Buffered->new($length);
$buf->print($bytes);

%package dev
Summary: dev components for the perl-Stream-Buffered package.
Group: Development
Provides: perl-Stream-Buffered-devel = %{version}-%{release}
Requires: perl-Stream-Buffered = %{version}-%{release}

%description dev
dev components for the perl-Stream-Buffered package.


%package license
Summary: license components for the perl-Stream-Buffered package.
Group: Default

%description license
license components for the perl-Stream-Buffered package.


%package perl
Summary: perl components for the perl-Stream-Buffered package.
Group: Default
Requires: perl-Stream-Buffered = %{version}-%{release}

%description perl
perl components for the perl-Stream-Buffered package.


%prep
%setup -q -n Stream-Buffered-0.03
cd %{_builddir}/Stream-Buffered-0.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Stream-Buffered
cp %{_builddir}/Stream-Buffered-0.03/LICENSE %{buildroot}/usr/share/package-licenses/perl-Stream-Buffered/0b7fcdfc9258e383c6ab16997817175947e4819a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Stream::Buffered.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Stream-Buffered/0b7fcdfc9258e383c6ab16997817175947e4819a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Stream/Buffered.pm
/usr/lib/perl5/vendor_perl/5.34.0/Stream/Buffered/Auto.pm
/usr/lib/perl5/vendor_perl/5.34.0/Stream/Buffered/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/Stream/Buffered/PerlIO.pm
