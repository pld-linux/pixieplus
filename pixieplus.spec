Summary:	pixieplus - image viewer for KDE
Summary(pl):	pixieplus - przegl±darka obrazków dla KDE
Name:		pixieplus
Version:	0.3
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.mosfet.org/pixie/%{name}-kde-%{version}.tar.gz
# Source0-md5:	28735cb48dfeb32e34e19f5f9ab9af29
Patch0:		%{name}-am16.patch
URL:		http://www.mosfet.org/pixie/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 3.1.4
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

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
%setup -q -n %{name}-kde-%{version}
#%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"
#%{__make} -f Makefile.cvs
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Graphics/*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers/

ln -s hicolor/48x48/apps/pixie.png $RPM_BUILD_ROOT%{_pixmapsdir}

for i in brightness+ brightness- contrast+ contrast- fliph flipv scaledown scaleup; do
	mv $RPM_BUILD_ROOT%{_pixmapsdir}/{lo,hi}color/16x16/actions/$i.png
done

for i in $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers/*.desktop; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_includedir}/*
%{_datadir}/apps/pixie
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/mimelnk/image/x-[!p]*.desktop
%{_datadir}/mimelnk/image/x-pict*.desktop
%{_applnkdir}/Graphics/Viewers/*.desktop
%{_pixmapsdir}/[!l]*/*/*/*.png
%{_pixmapsdir}/pixie.png
