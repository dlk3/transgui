# Building transgui for Fedora 41+

I have packaged [lighterowl's fork of transgui](https://github.com/lighterowl/transgui) for Fedora 41+ in my [Fedora COPR repository](https://copr.fedorainfracloud.org/coprs/dlk/transgui/).  If all you want to do is to install transgui using a package, you can do that from that repo.

## How to build your own Fedora package by hand

### Setup your RPM build environment

If you do not already have a RPM build environment on your system then you must set this up first:
```
# sudo dnf group install development-tools
# sudo dnf install rpmdevtools 
# rpmdev-setuptree
```
### Create a transgui source code tar file in your RPM build environment

1. Clone the source code:<br /><code>git clone --recurse-submodules https://github.com/lighterowl/transgui.git</code>
2. Search the  cloned <code>transgui/transgui.lpi</code> file for the <code>ProductVersion</code> string and use the value of that attribute as the transgui version number.  I'll use "5.18.8.f" as the example version number throughout the remainder of these instructions as that was the version number when I wrote this.
3. Add the desktop file I have provided to the cloned directory:<br /><code>cp transgui.desktop transgui/
4. Rename the cloned directory to <code>packagename-versionnumber</code> to conform with Fedora package standards:<br /><code>mv transgui transgui-5.18.8.f</code>
5. Create the source code tar file for this version of transgui in the proper directory in your RPM build environment:<br /><code>
tar -zcf ${HOME}/rpmbuild/SOURCES/transgui-5.18.8.f.tar.gz transgui-5.18.8.f</code>

### Build the package

1. Copy the <code>transgui.spec</code> file I have provided to the proper directory in your RPM build environment:<br /><code>cp transgui.spec ${HOME}/rpmbuild/SPECS/
2. Edit the <code>${HOME}/rpmbuild/SPECS/transgui.spec</code> and set <code>Version:</code> on the fourth line of the file to what you found in step 2 above.  You may also add a <code>%changelog</code> entry for this version at the bottom of the file if you wish.  Be careful, the [format](https://fedoraproject.org/wiki/PeterGordon/SpecFormattingGuidelines#RPM_ChangeLog_Entries) for the first line of each <code>%changelog</code> entry is very strict.
3. Install the pre-requisite packages required to compile transgui:<br><code>sudo dnf install lazarus fpc openssl-devel dbus-devel</code>
4. Build the transgui packages:<br /><code>rpmbuild -ba ${HOME}/rpmbuild/SPECS/transgui.spec</code>

### The package files
If the build completes successfully, the following package files will be in your RPM development environment directory tree:
```
${HOME}/rpmbuild/RPMS/x86_64/transgui-5.18.8.f-0.fc41.x86_64.rpm
${HOME}/rpmbuild/SRPMS/transgui-5.18.8.f-0.fc41.src.rpm
```
If you don't have these package files, examine the messages produced by the <code>rpmbuild</code> command closely to figure out what went wrong.
