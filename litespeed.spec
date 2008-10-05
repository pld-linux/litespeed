Summary:	LiteSpeed Web Server Standard Edition
Name:		litespeed
Version:	3.3.18
Release:	0.1
License:	"Free"
Group:		Networking/Daemons
Source0:	http://www.litespeedtech.com/packages/3.0/lsws-%{version}-std-i386-linux.tar.gz
# Source0-md5:	0da9eff04fda6486e493f3d454ef498d
URL:		http://www.litespeedtech.com/
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiteSpeed Web Server is the leading high-performance, high-scalability
web server. It is completely Apache interchangeable so LiteSpeed Web
Server can quickly replace a major bottleneck in your existing web
delivery platform. With its comprehensive range of features and
easy-to-use web administration console, LiteSpeed Web Server can help
you conquer the challenges of deploying an effective web serving
architecture.

%prep
%setup -q -n lsws-%{version}
# undos
%{__sed} -i -e 's,\r$,,' conf/httpd_config.xml.in

%{__sed} '
	s#%SERVER_NAME%#localhost#
	s#%ADMIN_EMAIL%#root@localhost#
	s#%USER%#http#
	s#%GROUP%#http#
	s#%PHP_BEGIN%##
	s#%PHP_SUFFIX%#php#
	s#%PHP_END%##
	s#%RUBY_BIN%#%{_bindir}/ruby#
' conf/httpd_config.xml.in > conf/httpd_config.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/%{name},%{_sbindir},/usr/lib/cgi-bin/%{name}}
cp -a conf/{httpd_config.xml,mime.properties,templates} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install bin/* $RPM_BUILD_ROOT%{_sbindir}
install fcgi-bin/*  $RPM_BUILD_ROOT/usr/lib/cgi-bin/%{name}
install admin/fcgi-bin/admin_php $RPM_BUILD_ROOT/usr/lib/cgi-bin/%{name}/lsphp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
