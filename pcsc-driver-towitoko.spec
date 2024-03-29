%define		pname	towitoko
Summary:	Unix driver for Towitoko smartcard readers
Summary(pl.UTF-8):	Uniksowy sterownik do czytników kart procesorowych Towitoko
Name:		pcsc-driver-towitoko
Version:	2.0.7
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.geocities.com/cprados/files/%{pname}-%{version}.tar.gz
# Source0-md5:	6cb2f842ca11aa79692af89d3730f4ce
URL:		http://www.geocities.com/cprados/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	pcsc-lite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a driver for using Towitoko smartcard readers
under UNIX environment.

Supported APIs: CT-API 1.1 and CT-BCS 0.9, PC/SC Lite.

Supported readers: Towitoko Chipdrive Micro, Extern, Extern II,
Intern, and Twin; serial and USB.

Supported smartcards: processor cards (direct and inverse convention,
T=0 and T=1 protocols), memory cards (I2C, 2-wire, 3-wire bus
protocol).

%description -l pl.UTF-8
Ta biblioteka dostarcza sterownik do używania czytników kart
procesorowych Towitoko w środowisku uniksowym.

Obsługiwane API: CT-API 1.1, CT-BCS 0.9, PC/SC Lite.

Obsługiwane czytniki: Towitoko Chipdrive Micro, Extern, Extern II,
Intern i Twin; podłączane do portu szeregowego lub USB.

Obsługiwane karty: procesorowe (w konwencji bezpośredniej lub
odwrotnej, protokoły T=0 i T=1), pamięciowe (protokoły I2C oraz z
szyną 2- i 3-liniową).

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
	--with-pcsc-lite-dir=/usr/lib/pcsc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}/pcsc/drivers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/{design.html,reader.conf}
%attr(755,root,root) %{_libdir}/pcsc/drivers/lib*.so*
