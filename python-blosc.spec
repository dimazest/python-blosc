%global __provides_filter_from ^%{python_sitearch}/.*\\.so$

%global	module	blosc

Summary:	Python wrapper for the blosc high performance compressor
Name:		python-%{module}
Version:	1.1
Release:	6%{?dist}
License:	MIT
URL:		https://github.com/FrancescAlted/python-blosc
Source0:	https://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	python2-devel blosc-devel


%description
Python wrapper for the Blosc high performance compressor.

%prep
%setup -q -n %{module}-%{version}

# Don't enable SSE2 optimizations
sed -i "s|CFLAGS\.append(\"-msse2\")|pass|" setup.py

%build
CFLAGS="%{optflags}" %{__python2} setup.py build 
# Fix lib perms
find . -name "blosc_extension.so" -exec chmod 0755 {} \;


%install
%{__python2} setup.py install --prefix=%{_prefix} -O1 --skip-build --root=%{buildroot}

%files
%{python2_sitearch}/blosc/
%{python2_sitearch}/blosc-%{version}*-py*.egg-info

%changelog
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
