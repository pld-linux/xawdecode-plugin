Summary:	Video4Linux Stream Capture Viewer and Descrambler
Name:		xawdecode-plugin
Version:	1.4.2
Release:	0.1
License:	GPL
Source0:	%{name}-%{version}.tar.gz
Group:		X11/Applications/Multimedia
Requires:	xawdecode >= 1.6.5
BuildRequires:	xawdecode-devel >= 1.6.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Descrambler plugin for Xawdecode

%package static
Summary:        Video4Linux Stream Capture Viewer and Descrambler
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description static
Descrambler plugin for Xawdecode. Static lib.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/divx" ; export CFLAGS
%configure --disable-ffmpeg --disable-alsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog Readme.txt lisez-moi
%doc FAQfr-xawdecode-plugin lisez-moi.txt FAQfr-xawdecode-plugin.txt
%doc lircrc.miro.sample lircrc.hauppauge.sample xawdecoderc.sample
%attr(755, root, root) %{_libdir}/lib*.so*
%{_libdir}/lib*.la
%{_mandir}/man1/*

%files static
%{_libdir}/lib*.a
