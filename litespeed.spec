Summary:	LiteSpeed Web Server Standard Edition
Name:		litespeed
Version:	3.3.18
Release:	0.1
License:	"Free"
Group:		Networking/Daemons
Source0:	http://www.litespeedtech.com/packages/3.0/lsws-%{version}-std-i386-linux.tar.gz
# Source0-md5:	0da9eff04fda6486e493f3d454ef498d
URL:		http://www.litespeedtech.com/
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

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
