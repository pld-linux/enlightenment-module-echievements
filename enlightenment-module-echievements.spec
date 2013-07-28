Summary:	Echievements module for E17
Summary(pl.UTF-8):	Moduł Echievements dla E17
Name:		enlightenment-module-echievements
Version:	3
Release:	2
License:	BSD
Group:		Applications
Source0:	http://download.enlightenment.org/releases/echievements-%{version}.tar.bz2
# Source0-md5:	401aceb812611440de4374e133c8f9be
Patch0:		%{name}-am.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	enlightenment-devel >= 0.17
BuildRequires:	etrophy-devel >= 0.5.1
BuildRequires:	gettext-devel >= 0.14
BuildRequires:	libtool
BuildRequires:	pkgconfig
%requires_eq_to	enlightenment enlightenment-devel
Requires:	etrophy >= 0.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Echievements provides achievements for E17. It is a module that serves
as nothing more than a very entertaining time-waster.

%description -l pl.UTF-8
Echievements udostępnia zdobycze dla E17. Jest to moduł służący
wyłącznie jako przyciągający zabijacz czasu.

%prep
%setup -q -n echievements-%{version}
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/enlightenment/modules/echievements/linux-gnu-*/module.la

%find_lang echievements

%clean
rm -rf $RPM_BUILD_ROOT

%files -f echievements.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%dir %{_libdir}/enlightenment/modules/echievements
%{_libdir}/enlightenment/modules/echievements/e-module-echievements.edj
%{_libdir}/enlightenment/modules/echievements/module.desktop
%{_libdir}/enlightenment/modules/echievements/trophy.png
%dir %{_libdir}/enlightenment/modules/echievements/linux-gnu-*
%{_libdir}/enlightenment/modules/echievements/linux-gnu-*/module.so
