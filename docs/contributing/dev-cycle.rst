Development Cycle
=================

This document is more for repository administrators, but those interested may still like to know this stuff.

Versioning
----------

The versioning scheme will follow this scheme. For builds where nothing is ready yet, use the `pre-alpha-X` scheme. The `X` is any number. Since the author of this document is a chad C enjoyer, `X` will be zero-indexed. Therefore, the first possible build will be `pre-alpha-0`. During the pre-alpha phase, these will be weekly releases as long as versions differ. Once there is something workable, development will switch to `alpha-X`. Again, `X` will be any number, starting from 0. This will continue until all necessary features have been finished. This will begin the `beta-X` phase. Here, `X` will again be any number starting from zero. This number will be incremented after every major change. After this phase has been reached, there will be a new branch tracking weekly changes. At a certain point, the release canditates phase will start. This will happen when the product could be released in the current state, but bugs or missing features cause the project to be less than acceptable. In this phase, versions will be denoted using the `vX.Y.Z`, where `X`, `Y`, and `Z` are any number starting from zero. During development of a version with these numbers, we will use a release candidate system, which will have numbers looking like `vX.Y.Z-build-XXXX`. If it ever comes down to it, these versions may also be suffixed with extra information regarding compatibility, such as `v2.1.3-fabric` for a modpack that works with Fabric mod loader, or `v3.5-m63k` for a version that will work on TI-89 calculators with a Motorola 63000 series processor.
