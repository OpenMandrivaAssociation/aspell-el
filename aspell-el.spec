%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-3
%define languageeng greek
%define languageenglazy Greek
%define languagecode el

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.3
Release:	28
Group:		System/Internationalization
License:	GPLv2
Url:		https://aspell.sourceforge.net/
Source0:	ftp://ftp.gnu.org/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-el
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install

%makeinstall_std

chmod 644 README Copyright

%files
%doc README Copyright
%{_libdir}/aspell-*/*

