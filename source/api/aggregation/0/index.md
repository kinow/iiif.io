---
title: "Aggregation, Discovery, and Import API"
title_override: "IIIF Aggregation, Discovery, and Import API"
id: discovery-aggregation
layout: spec
tags: [specifications, discovery-aggregation]
major: 0
minor: 1
patch: 0
pre: draft
redirect_from:
  - /api/aggregation/index.html
---

## Status of this Document
{:.no_toc}

__This Version:__ {{ page.major }}.{{ page.minor }}.{{ page.patch }}{% if page.pre != 'final' %}-{{ page.pre }}{% endif %}

__Latest Stable Version:__ None

**Editors:**

  * **[Michael Appleby](https://orcid.org/0000-0002-1266-298X)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0002-1266-298X), [_Yale University_](http://www.yale.edu/)
  * **[Tom Crane](https://orcid.org/0000-0003-1881-243X)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0003-1881-243X), [_Digirati_](http://digirati.com/)
  * **[Robert Sanderson](https://orcid.org/0000-0003-4441-6852)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0003-4441-6852), [_Stanford University_](http://www.stanford.edu/)
  * **[Jon Stroop](https://orcid.org/0000-0002-0367-1243)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0002-0367-1243), [_Princeton University Library_](https://library.princeton.edu/)
  * **[Simeon Warner](https://orcid.org/0000-0002-7970-7855)** [![ORCID iD](/img/orcid_16x16.png)](https://orcid.org/0000-0002-7970-7855), [_Cornell University_](https://www.cornell.edu/)
  {: .names}

{% include copyright.md %}

----

## Table of Contents
{:.no_toc}

* Table of Discontent (will be replaced by macro)
{:toc}

## 1. Introduction

### Audience and Scope
 * Carefully acknowledge somehow that this extends the scope of IIIF, but is at least controlled mission creep (i.e. similar to a controlled burn :-))

 * Use cases:
    * thematic registries and portals
    * ad-hoc reuse/remixing/mashups
    * NOT indended for transmission ( METS)

### Terminology

 * distinguish bet. aggregation, discovery, and import
 * Sitemaps
 * refs to other specs (for eg. seeAlso),
 * RFC 2119 keywords

## 2. Aggregation

 * Via sitemaps, optionally w/ ResourceSync extensions
 * Distinct from curated collections in that they're just a list.
    * No repetiton
    * No order
    * No hierarchy
    * (Not necessarily thematic, no labels)

## 3. Discovery

 * (happens after aggregation)
 * seeAlso profiles

## 4. Import

(i.g. drag & drop - you've found this thing, now what?)
 * Start with http://zimeon.github.io/iiif-dragndrop/
 * Maybe doesn't belong here, it's a little disjoint, but maybe easier than a separate spec
 * Logo use
    * IIIF Logo
    * Source Institution Logo (per Prezi spec))
