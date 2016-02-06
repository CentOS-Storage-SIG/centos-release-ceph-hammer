centos-release-ceph-hammer provides the YUM repository file for packages of the
CentOS Storage SIG that are used with Ceph Hammer (0.94.x).

Building the package can be done like this:


    $ rpmbuild -bs
               --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" \
               --define "dist .el7" \
               centos-release-ceph-hammer.spec

    $ koji -p cbs \
           build storage7-ceph-hammer-el7 \
           centos-release-ceph-hammer-1.0-2.el7.src.rpm

