Summary:	pixieplus - image viewer for KDE
Summary(pl):	pixieplus - przegl±darka obrazków dla KDE
Name:		pixieplus
Version:	0.5.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.mosfet.org/pixie/%{name}-%{version}.tar.gz
# Source0-md5:	a6296cdc53b5f1a38cd629f7591fef9e
#Patch0:		%{name}-am16.patch
URL:		http://www.mosfet.org/pixie/
BuildRequires:	ImageMagick-c++-devel >= 5.5.0
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.1
Requires:  	ImageMagick-c++ >= 5.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML
%define		_prefix		%{_usr}

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
#%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"
#%%{__make} -f Makefile.cvs
%configure	\
	--enable-final
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Graphics/*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
##{_includedir}/*
%{_datadir}/apps/pixie
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/mimelnk/image/x-miff.desktop
##{_datadir}/mimelnk/image/x-pcx.desktop
%{_datadir}/mimelnk/image/x-pict.desktop
%{_datadir}/mimelnk/image/x-tga.desktop
%{_datadir}/mimelnk/image/x-xwd.desktop
%{_applnkdir}/Graphics/Viewers/*.desktop
%{_pixmapsdir}/*/*/*/*.png
