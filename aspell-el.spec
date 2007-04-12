%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-3
%define languageeng greek
%define languageenglazy Greek
%define languagecode el

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.3
Release:       %mkrel 7
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-el

BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

# Mandrake Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-*/*


