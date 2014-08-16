%{?scl:%scl_package python-blosc}
%{!?scl:%global pkg_name %{name}}

%global	module	blosc

Summary:	Python wrapper for the blosc high performance compressor
Name:		%{?scl_prefix}python-%{module}
Version:	1.2.4
Release:	1%{?dist}
License:	MIT
URL:		https://github.com/FrancescAlted/python-blosc
Source0:	https://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz

%{?scl:Requires: %{scl}-runtime}

BuildRequires:	%{?scl_prefix}python-devel %{?scl_prefix}blosc-devel
%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}

BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Python wrapper for the Blosc high performance compressor.

%prep
%setup -q -n %{pkg_name}-%{version}

# Don't enable SSE2 optimizations
sed -i "s|CFLAGS\.append(\"-msse2\")|pass|" setup.py

%build
%{?scl:scl enable %{scl} - << \EOF}
export BLOSC_DIR=%{_prefix}
CFLAGS="%{optflags}" %{__python3} setup.py build
%{?scl:EOF}

# Fix lib perms
find . -name "blosc_extension.so" -exec chmod 0755 {} \;

%install
%{?scl:scl enable %{scl} "}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
%{?scl:"}

%files
%{python3_sitearch}/blosc/
%{python3_sitearch}/blosc-%{version}*-py*.egg-info

%changelog
* Sat Aug 16 2014 Dmitrijs Milajevs <dimazest@gmail.com> - 1.2.4-1
- Cleanup and adoptations for Software collections.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-2
- Rebuild for blosc

* Sat Mar 22 2014 Thibault North <tnorth@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3 for blosc 1.3.4

* Wed Jan 08 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-8
- Rebuild for blosc

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-7
- Properly link with blosc shared lib

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-6
- Disable SSE2 optimizations

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-5
- Final cosmetic fixes

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-4
- Fix wrong lib perms

* Fri Oct 18 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-3
- Fixes, thanks to Christopher Meng

* Wed Oct 16 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-2
- Various fixes

* Fri Sep 20 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-1
- Sync to version 1.1

* Mon Jan 2 2012 Thibault North <tnorth@fedoraproject.org> - 1.0.7-1
- Initial package
