Name:           ratbagd
Version:        0.3
Release:        1%{?dist}
Summary:        System daemon to access configurable mice

License:        MIT
URL:            https://github.com/libratbag/ratbagd
Source0:        https://github.com/libratbag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake libtool
BuildRequires:  python3-devel
BuildRequires:  libratbag-devel >= 0.4
BuildRequires:  systemd systemd-devel >= 227
BuildRequires:  meson >= 0.40

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
%autosetup

%build
export PYTHON="python3"
%meson -Dsystemd-unit-dir=%{_unitdir}
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/ratbagd
%{_unitdir}/ratbagd.service
%{_datadir}/dbus-1/system-services/org.freedesktop.ratbag1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.ratbag1.conf
%{_mandir}/man1/ratbagctl.1*
%{_mandir}/man8/ratbagd.8*

%files python
%{_bindir}/ratbagctl
%{python3_sitelib}/%{name}

%changelog
* Fri May 12 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.3-1
- ratbagd 0.3

* Wed Mar 22 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.2-4
- Rebuild for new libratbag

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

