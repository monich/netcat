Name:       netcat
Summary:    The networking swiss army knife
Version:    0.7.1
Release:    1
Group:      System/Tools
License:    GPLv2
URL:        http://netcat.sourceforge.net/
Source0:    %{name}-%{version}.tar.bz2

%description
Netcat is a featured networking utility which reads and writes data
across network connections, using the TCP/IP protocol. It is designed
to be a reliable "back-end" tool that can be used directly or easily
driven by other programs and scripts. At the same time, it is a
feature-rich network debugging and exploration tool, since it can
create almost any kind of connection you would need and has several
interesting built-in capabilities.

%prep
%setup -q

%build
%reconfigure --prefix=%{_prefix} --disable-nls
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/nc
%{_bindir}/netcat
