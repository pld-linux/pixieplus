Summary:	pixieplus - image viewer for KDE
Summary(pl):	pixieplus - przegl�darka obrazk�w dla KDE
Name:		pixieplus
Version:	0.5.4
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://people.fruitsalad.org/avleeuwen/distfiles/pixieplus/%{name}-%{version}.tar.gz
# Source0-md5:	a6296cdc53b5f1a38cd629f7591fef9e
Patch0:		%{name}-types.patch
URL:		http://people.fruitsalad.org/avleeuwen/distfiles/pixieplus/
BuildRequires:	ImageMagick-c++-devel >= 5.5.0
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libltdl-devel
BuildRequires:	qt-devel >= 3.1
Requires:	ImageMagick-c++ >= 5.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Pixie is designed to allow you to efficently browse, manage, and view
large numbers of images as well as do basic editing such as adjust
contrast/brightness, scale, and apply effects. For Windows users, you
can think of it as a combination of ACDSee(TM) and Paint Shop Pro(TM).

%description -l pl
Pixie jest narz�dziem s�u��cym do przegl�dania i zarz�dzania du��
ilo�ci� plik�w graficznych umo�liwiaj�cym prost� edycj� obraz�w
(poziomy jasno�ci i kontrastu, skalowanie oraz efekty dodatkowe).

%prep
%setup -q
%patch0 -p1

echo 'Categories=Graphics;Viewer;' >> desktopfiles/pixie.desktop
echo 'Categories=Graphics;Viewer;' >> desktopfiles/pixie-mini.desktop

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}

# no -devel, so shouldn't be needed
rm -f $RPM_BUILD_ROOT%{_libdir}/libpixie_misc.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpixie_misc.so.*.*.*
%attr(755,root,root) %{_libdir}/pixie.so
%{_libdir}/pixie.la
##{_includedir}/*
%{_datadir}/apps/pixie
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/mimelnk/image/x-miff.desktop
##{_datadir}/mimelnk/image/x-pcx.desktop
%{_datadir}/mimelnk/image/x-pict.desktop
%{_datadir}/mimelnk/image/x-tga.desktop
%{_datadir}/mimelnk/image/x-xwd.desktop
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/*.png
