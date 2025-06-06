# Building transgui for Fedora 41+

I have packaged [lighterowl's fork of transgui](https://github.com/lighterowl/transgui) for Fedora 41+ in my [Fedora COPR repository](https://copr.fedorainfracloud.org/coprs/dlk/transgui/).  If all you want to do is to install transgui on Fedora using a RPM package, you can do that from that repo.

## How to build your own Fedora package by hand

Building this version of transgui requires development versions of the Free Pascal Compiler (fpc) and its IDE tool Lazarus.  As far as I can tell, these development versions of these applications are not available from any Fedora repository.  They must be built and installed manually before they can be used to compile and build a RPM package for transgui.

I have provided a script called <code>build</code> and an associated <code>Dockerfile</code> that will perform the steps necessary to build an RPM for transgui within a podman (Docker) container on a Fedora system.  As well as being run directly, this script can function as a recipe for manually building a transgui RPM package.
