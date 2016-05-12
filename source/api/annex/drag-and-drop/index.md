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
This document describes a pattern for the implementation of drag and drop fuctionality for IIIF Presentation API and Image API resources.

Please send feedback to [iiif-discuss@googlegroups.com][iiif-discuss]

## Table of Contents
{:.no_toc}

* Table of Discontent (will be replaced by macro)
{:toc}

## 1. Introduction

Use case "Add to viewer": User has a Mirador window open (or other IIIF multi-up viewer). In another window, the user is browsing or using a search interface, and locates an image, book, manuscript, etc. that they want to view in Mirador. The page for that object includes an IIIF icon that they drag and drop to Mirador. Mirador then adds the image/manifest to its index and displays it. The user can then repeat this at another site to add additional images, perhaps adding a set of different witnesses of a manuscript that they wish to compare.

Use case "Add to manifest": User has an IIIF application open providing the ability to edit a collection of images/canvases (manifest). (such facilities might be added to Mirador or UniversalViewer). In another window, the user is browsing or using a search interface, and locates an image that they want to add to the collection of images they are creating. The page for that image includes an IIIF icon that they drag and drop to their application. Their application adds the image dropped in to the collection. (The image dropped in might be a single IIIF image, or it might be one image from a larger set described by a manifest in which case other metadata can be copied also).

## 2. Implementation in HTML

The source page for drag and drop should include the standard IIIF logo wrapped in a hyperlink. The URI of the hyperlink provides a default target in case clicked by the user, followed by a dummy query string with the manifest, canvas or image info.json URIs used to implement the draf and drop. The default target could be a help page or perhaps open a particular viewer showing the image or manifest. The query parameters are:

  * `manifest` - URI of an IIIF Presentation API manifest.
  * `canvas` - URI of currently selected canvas within the manifest. If no canvas is specified then the target application will use its default behaviour to present the manifest. (Has no meaning unless manifest is given.)
  * `image` - URI of an IIIF Image API info.json. This is an alternative to specifying a manifest for use in situations where the source implements only the Image API.

HTML example:

``` html
<a href="default_target?manifest=manifest_URI&canvas=canvas_URI"
   alt="Drag and drop this icon to an IIIF application">
  <img src="iiif-dragndrop-100px.png" alt="IIIF Drag and drop"/>
</a>
```

### 3. Icon

The current best-practice is to use a version of the IIIF logo as the 

### A. Acknowledgments

The drag and drop pattern described here was devised by Drew Winget, Mark Matienzo, Simeon Warner, and others at the IIIF Shimathon 2015-09-29/30, hosted by the Univeristy of Pennsylvania. The pattern was then implemented within the Mirador and Universal Viewer browsing applications.

### B. Change Log

| Date       | Description                                        |
| ---------- | -------------------------------------------------- |
| 2016-05-12 | Version 1.0                                        |

   [semver]: /api/annex/notes/semver/ "Versioning of APIs"
   [iiif-discuss]: mailto:iiif-discuss@googlegroups.com "Email Discussion List"
   [image-api]: /api/image/{{ site.image_api.latest.major }}.{{ site.image_api.latest.minor }}/ "Image API"
   [prezi-api]: /api/presentation/{{ site.presentation_api.latest.major }}.{{ site.presentation_api.latest.minor }}/ "Presentation API"
   [mirador]: http://projectmirador.org/ "Mirador"
   [uv]: https://github.com/UniversalViewer/universalviewer "Universal Viewer"

{% include acronyms.md %}
