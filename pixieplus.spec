Summary:	pixieplus - image viewer for KDE
Summary(pl):	pixieplus - przegl±darka obrazków dla KDE
Name:		pixieplus
Version:	0.5.4.1
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://people.fruitsalad.org/avleeuwen/distfiles/pixieplus/%{name}-%{version}.tar.bz2
# Source0-md5:	5a7b98acef2af9cdf6a0b546cada562a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-bool.patch
Patch2:		%{name}-gcc34.patch
URL:		http://people.fruitsalad.org/avleeuwen/distfiles/pixieplus/
BuildRequires:	ImageMagick-c++-devel >= 6.0.0
BuildRequires:	automake
BuildRequires:	giflib-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	ImageMagick-c++ >= 6.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pixie is designed to allow you to efficently browse, manage, and view
large numbers of images as well as do basic editing such as adjust
contrast/brightness, scale, and apply effects. For Windows users, you
can think of it as a combination of ACDSee(TM) and Paint Shop Pro(TM).

%description -l pl
Pixie jest narzêdziem s³u¿±cym do przegl±dania i zarz±dzania du¿±
ilo¶ci± plików graficznych umo¿liwiaj±cym prost± edycjê obrazów
(poziomy jasno¶ci i kontrastu, skalowanie oraz efekty dodatkowe).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--enable-final \
	--with-qt-libraries=%{_libdir}

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
%{_datadir}/apps/pixie
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/mimelnk/image/x-miff.desktop
##{_datadir}/mimelnk/image/x-pcx.desktop
%{_datadir}/mimelnk/image/x-pict.desktop
%{_datadir}/mimelnk/image/x-tga.desktop
%{_datadir}/mimelnk/image/x-xwd.desktop
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
