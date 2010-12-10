%define major 0
%define libname %mklibname srs_alt %{major}
%define develname %mklibname srs_alt -d

Summary:	A C implementation of SRS
Name:		libsrs_alt
Version:	0.5
Release:	%mkrel 7
License:	GPL
Group:		System/Libraries
URL:		http://srs.mirtol.com/
Source0:	http://srs.mirtol.com/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
Provides:	%{name}-devel = %{version}-%{release}
Provides:	srs_alt-devel = %{version}-%{release}
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

mv %{buildroot}%{_bindir}/srs %{buildroot}%{_bindir}/srs_alt

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h

%files -n %{name}-utils
%defattr(-,root,root)
%{_bindir}/srs_alt
