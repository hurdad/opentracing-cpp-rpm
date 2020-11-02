Name:           opentracing-cpp
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        C++ implementation of the OpenTracing API http://opentracing.io
Group:          System Environment/Libraries
License:	Apache 2.0
URL:            https://github.com/opentracing/opentracing-cpp
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3

%description
C++ implementation of the OpenTracing API http://opentracing.io

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup

%build 
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=lib64

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md 
%{_libdir}/libopentracing.so.*
%{_libdir}/libopentracing_mocktracer.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/opentracing
%{_libdir}/cmake/OpenTracing/*.cmake

%changelog
