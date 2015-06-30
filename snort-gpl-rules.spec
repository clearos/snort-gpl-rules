Name: snort-gpl-rules
Version: 2.9.0.8
Release: 2%{dist}
License: GPL
Group: Applications/System
Packager: ClearFoundation
Source: %{name}-%{version}.tar.gz
Patch1: snort-gpl-rules-2.9.0.8-updates.patch
Requires: /sbin/service
Requires: snort
BuildArch: noarch
Summary: GPL intrusion detection and prevention rules

%description
GPL intrusion detection and prevention rules.

The most recent rules from SourceFire are only available to those with a
Sourcefire VRT subscription.  The rules included in this package are GPL
but somewhat obsolete.

%prep
%setup -q
%patch1 -p1
%build

%install
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/snort.d/rules/gpl
cp * %{buildroot}%{_sysconfdir}/snort.d/rules/gpl/

%post
if [ $1 -eq 1 ]; then
    /sbin/service snort condrestart >/dev/null 2>&1
fi

exit 0

%preun
if [ $1 -eq 0 ]; then
    /sbin/service snort condrestart >/dev/null 2>&1
fi

exit 0

%postun
if [ $1 -ge 1 ]; then
    /sbin/service snort condrestart >/dev/null 2>&1
fi

exit 0

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/snort.d/rules/gpl
%{_sysconfdir}/snort.d/rules/gpl/*.rules
%{_sysconfdir}/snort.d/rules/gpl/LICENSE_GPLv2
