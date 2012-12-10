%define major 0
%define libname %mklibname srs_alt %{major}
%define develname %mklibname srs_alt -d

Summary:	A C implementation of SRS
Name:		libsrs_alt
Version:	0.5
Release:	8
License:	GPL
Group:		System/Libraries
URL:		http://srs.mirtol.com/
Source0:	http://srs.mirtol.com/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	libtool

%description
libsrs_alt is a C implementation of SRS (Sender Rewriting Scheme)

Features:

 o No external library requirements (from 0.4)
 o Quick and easy to use library interface
 o Support for database callback with SRS0
 o srs command line tool and srs daemon
 o All non-critical errors reported using function return value
 o Support for Exim (including database lookup) (See latest exiscan patch)
 o SRS Compliant
 o Automake/autoconf package 

%package -n	%{libname}
Summary:	A C implementation of SRS
Group:		System/Libraries

%description -n	%{libname}
libsrs_alt is a C implementation of SRS (Sender Rewriting Scheme)

Features:

 o No external library requirements (from 0.4)
 o Quick and easy to use library interface
 o Support for database callback with SRS0
 o srs command line tool and srs daemon
 o All non-critical errors reported using function return value
 o Support for Exim (including database lookup) (See latest exiscan patch)
 o SRS Compliant
 o Automake/autoconf package 

%package -n	%{develname}
Summary:	Development tools needed to build programs that use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	srs_alt-devel = %{EVRD}
Obsoletes:	%{mklibname srs_alt 0 -d}

%description -n	%{develname}
libsrs_alt is a C implementation of SRS (Sender Rewriting Scheme)

This package contains development files needed to compile softwares
against the libsrs_alt library.

%package -n	%{name}-utils
Summary:	Command line interface to %{name}
Group:		System/Servers

%description -n	%{name}-utils
Command line interface to %{name}

%prep

%setup -q

%build

%configure2_5x

make

%install
%makeinstall_std

mv %{buildroot}%{_bindir}/srs %{buildroot}%{_bindir}/srs_alt

%files -n %{libname}
%doc ChangeLog
%{_libdir}/lib*.so.*

%files -n %{develname}
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

%files -n %{name}-utils
%{_bindir}/srs_alt


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-7mdv2011.0
+ Revision: 620228
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-6mdv2010.0
+ Revision: 429833
- rebuild

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 0.5-5mdv2009.0
+ Revision: 250580
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5-3mdv2008.1
+ Revision: 136566
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-3mdv2008.0
+ Revision: 83773
- new devel naming


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5-2mdv2007.0
+ Revision: 93739
- Import libsrs_alt

* Sat Apr 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5-2mdk
- rebuild

* Thu Mar 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial package

