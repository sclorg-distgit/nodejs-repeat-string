%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name repeat-string

Summary:       Repeat the given string n times
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:        1.6.1
Release:        1%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/repeat-string
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Repeat the given string n times. 
Fastest implementation for repeating a string.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Oct 31 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.6.1-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.2-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.2-3
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.5.2-2
- Enable scl macros

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com> - 1.5.2-1
- Initial package
