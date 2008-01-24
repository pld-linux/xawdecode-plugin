Summary:	Video4Linux Stream Capture Viewer and Descrambler
Summary(pl.UTF-8):	Program do oglądania i dekodowania strumieni Video4Linux
Name:		xawdecode-plugin
Version:	1.4.8
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://cricrac.free.fr/download/xawdecode/stable/%{name}-%{version}.tar.gz
# Source0-md5:	960caf729c88f12ec2cb3b247c7b6bfd
URL:		http://cricrac.free.fr/
BuildRequires:	xawdecode-devel >= 1.8.0
Requires:	xawdecode >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Descrambler plugin for Xawdecode.

%description -l pl.UTF-8
Wtyczka dekodująca dla Xawdecode.

%package static
Summary:	Video4Linux Stream Capture Viewer and Descrambler
Summary(pl.UTF-8):	Program do oglądania i dekodowania strumieni Video4Linux
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description static
Descrambler plugin for Xawdecode. Static lib.

%description static -l pl.UTF-8
Wtyczka dekodująca dla Xawdecode - biblioteka statyczna.

%prep
%setup -q

%build
%configure \
	--disable-divx4linux \
	--disable-alsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS ChangeLog Readme.txt lisez-moi
%doc FAQfr-xawdecode-plugin lisez-moi.txt FAQfr-xawdecode-plugin.txt
%doc lircrc.miro.sample lircrc.hauppauge.sample xawdecoderc.sample
%attr(755, root, root) %{_libdir}/lib*.so*
%{_libdir}/lib*.la
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
