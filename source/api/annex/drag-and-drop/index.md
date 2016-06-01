---
title: Drag and Drop for IIIF Resources
layout: spec
tags: [annex, specifications]
cssversion: 2
---

## Status of this Document
{:.no_toc}

This document is not subject to [semantic versioning][semver].
Changes will be tracked within the document.

**Editors**

  * **[Michael Appleby](https://orcid.org/0000-0002-1266-298X)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0002-1266-298X), [_Yale University_](http://www.yale.edu/)
  * **[Tom Crane](https://orcid.org/0000-0003-1881-243X)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0003-1881-243X), [_Digirati_](http://digirati.com/)
  * **[Robert Sanderson](https://orcid.org/0000-0003-4441-6852)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0003-4441-6852), [_Stanford University_](http://www.stanford.edu/)
  * **[Jon Stroop](https://orcid.org/0000-0002-0367-1243)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0002-0367-1243), [_Princeton University Library_](https://library.princeton.edu/)
  * **[Simeon Warner](https://orcid.org/0000-0002-7970-7855)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0002-7970-7855), [_Cornell University_](https://www.cornell.edu/)
  {: .names}

{% include copyright2016.md %}

## Abstract
{:.no_toc}
This document describes a pattern for the implementation of drag and drop fuctionality for [IIIF Presentation API][prezi-api] and [Image API][image-api] resources.

Please send feedback to [iiif-discuss@googlegroups.com][iiif-discuss]

## Table of Contents
{:.no_toc}

* Table of Discontent (will be replaced by macro)
{:toc}

## 1. Introduction

Drag and drop has been a standard feature of desktop user interfaces for some time, and more recently a feature of web applications. This note describes a pattern for the implementation of drag and drop fuctionality for [IIIF Presentation API][prezi-api] and [Image API][image-api] resources. The pattern was motivated by need for broad cross-browser support and the following two use cases:

  * **Add to viewer**: User has an IIIF multi-up viewer window open. In another window, the user is browsing or using a search interface, and locates an image, book, manuscript, etc. that they want to view. The page for that object includes an IIIF icon that they drag and drop to the viewer. The viewer then adds the image/manifest to its index and displays it. The user can then repeat this at another site to add additional images, perhaps adding a set of different witnesses of a manuscript that they wish to compare.
  * **Add to manifest**: User has an IIIF application open providing the ability to edit a collection of images/canvases (manifest). In another window, the user is browsing or using a search interface, and locates an image that they want to add to the collection of images they are creating. The page for that image includes an IIIF icon that they drag and drop to their application. Their application adds the image dropped in to the collection. (The image dropped in might be a single IIIF image, or it might be one image from a larger set described by a manifest in which case other metadata can be copied also).

## 2. Source Implementation in HTML

The source page for drag and drop should include an [icon](#icon) wrapped in a hyperlink. The URI of the hyperlink provides a default target in case the link is clicked by the user (rather than dragged), followed by a dummy query string with the `manifest`, `canvas` or `image` `info.json` URIs used to implement the drag and drop. The default target could be a help page or perhaps open a particular viewer showing the image or manifest. The query parameters are:

  * `manifest` - URI of an IIIF Presentation API manifest.
  * `canvas` - URI of currently selected canvas within the manifest. If no canvas is specified then the target application will use its default behaviour to present the manifest. (Has no meaning unless `manifest` is also given.)
  * `image` - URI of an IIIF Image API `info.json`. This is an alternative to specifying a manifest for use in situations where the source implements only the Image API.

HTML example using `manifest` and `canvas` to support drag and drop of a manifest with a particular canvas selected:

``` html
<a href="default_target?manifest=manifest_URI&canvas=canvas_URI"
   alt="Drag and drop this icon to an IIIF application">
  <img src="iiif-dragndrop-100px.png" alt="IIIF Drag and drop"/>
</a>
```

HTML example using `image` to support drag and drop of a single image resource:

``` html
<a href="default_target?image=image_URI"
   alt="Drag and drop this icon to an IIIF application">
  <img src="iiif-dragndrop-100px.png" alt="IIIF Drag and drop"/>
</a>
```

## 3. Icon

The current best-practice is to use a version of the IIIF logo as the icon for drag and drop. FIXME - NEED STANDARD LOCATION FOR ICON, AND SIZE.

## 4. Destination Implementation

FIXME - WHAT SHOULD BE SPECIFIED? SHOULD WE INCLUDE TEST IMPLEMENTATION LIKE <http://zimeon.github.io/iiif-dragndrop/droptest.html>?

## A. Acknowledgments

The drag and drop pattern described here was devised by Drew Winget, Mark Matienzo, Simeon Warner, and others at the IIIF Shimathon 2015-09-29/30, hosted by the Univeristy of Pennsylvania. The pattern was then implemented within the Mirador and Universal Viewer browsing applications.

## B. Change Log

| Date       | Description                                        |
| ---------- | -------------------------------------------------- |
| 2016-08-xx | Version 1.0                                        |

   [semver]: /api/annex/notes/semver/ "Versioning of APIs"
   [iiif-discuss]: mailto:iiif-discuss@googlegroups.com "Email Discussion List"
   [image-api]: /api/image/{{ site.image_api.latest.major }}.{{ site.image_api.latest.minor }}/ "Image API"
   [prezi-api]: /api/presentation/{{ site.presentation_api.latest.major }}.{{ site.presentation_api.latest.minor }}/ "Presentation API"
   [mirador]: http://projectmirador.org/ "Mirador"
   [uv]: https://github.com/UniversalViewer/universalviewer "Universal Viewer"

{% include acronyms.md %}
