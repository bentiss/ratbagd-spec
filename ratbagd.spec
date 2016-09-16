%global libsystemd_version 229

Name:           ratbagd
Version:        0.2
Release:        3%{?dist}
Summary:        System daemon to access configurable mice

License:        MIT
URL:            https://github.com/libratbag/ratbagd
Source0:        https://github.com/libratbag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake libtool
BuildRequires:  python3-devel
BuildRequires:  libratbag-devel >= 0.4
%if 0%{?fedora} <= 23
BuildRequires:  libsystemd libsystemd-devel == 229
BuildRequires:  systemd systemd-devel
%else
BuildRequires:  systemd systemd-devel >= 227
%endif

%description
%{name} is a system daemon that exports libratbag-compatible devices over DBus,
allowing nonprivileged applications to introspect and configure those
devices.

%package python
Summary:        System daemon to access configurable mice Python bindings
Provides:       python3-ratbagd
BuildArch:      noarch

%description python
Python bindings to %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf --force -v --install || exit 1
export PYTHON="python3"

%if 0%{?fedora} <= 23
export PKG_CONFIG_PATH="%{_libdir}/libsystemd-%{libsystemd_version}/pkgconfig"
%endif

%configure --disable-silent-rules \
           --with-systemd-unit-dir=%{_unitdir}
make %{?_smp_mflags}

%install
%make_install
%if 0%{?fedora} == 22
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.ratbag1.conf \
	%{buildroot}%{_sysconfdir}/dbus-1/system.d/org.freedesktop.ratbag1.conf
%endif

%files
%doc COPYING
%{_bindir}/ratbagd
%config %{_unitdir}/ratbagd.service
%{_datadir}/dbus-1/system-services/org.freedesktop.ratbag1.service
%if 0%{?fedora} > 22
%{_datadir}/dbus-1/system.d/org.freedesktop.ratbag1.conf
%else
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.ratbag1.conf
%endif

%files python
%{_bindir}/ratbagctl
%{python3_sitelib}/%{name}/*

%changelog
* Fri Sep 16 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.2-3
- Rebuild for new libratbag

* Thu Mar 17 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.2-2
- Fix "Permission denied" on F22

* Wed Mar 16 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.2-1
- ratbagd 0.2

* Mon Mar 14 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.1.2-2
- compile for f22 too

* Mon Mar 14 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.1.2-1
- ratbagd 0.1.2

* Thu Mar 10 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.1-1
- ratbagd 0.2

* Wed Mar 09 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.0.2-3
- fix Fedora 23 detection

* Tue Mar 08 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.0.2-2
- Enable F23 builds with systemd < 227

* Tue Mar 08 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.0.2-1
- Initial release

