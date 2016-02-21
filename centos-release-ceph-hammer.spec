Summary: Ceph Hammer packages from the CentOS Storage SIG repository
Name: centos-release-ceph-hammer
Version: 1.0
Release: 4%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Ceph-Hammer.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Users can install centos-release-ceph to get the latest
Provides: centos-release-ceph = 0.94
Conflicts: centos-release-ceph < 0.94
Obsoletes: centos-release-ceph < 0.94

%description
yum configuration for Ceph Hammer (0.94.x) packages as delivered via the CentOS
Storage SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Ceph-Hammer.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Ceph-Hammer.repo

%changelog
* Sun Feb 21 2016 François Cami <fcami@fedoraproject.org> - 1.0-4
- Add -source and -debuginfo repositories

* Sat Feb 20 2016 François Cami <fcami@fedoraproject.org> - 1.0-3
- Bump release

* Sat Feb 06 2016 François Cami <fcami@fedoraproject.org> - 1.0-2
- Bump release

* Wed Jan 27 2016 François Cami <fcami@fedoraproject.org> - 1.0-1
- Initial version based on centos-release-gluster37

