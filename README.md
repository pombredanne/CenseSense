CenseSense
==========

CenseSense is an open-source application that aims to help alleviate developers from the legal hassles of software licenses, and having to be ever-wary of the types of projects they 
include in their source-code. Just  point CenseSense's configuration to your project folders, run CenseSense in your preffered language (more always incoming), and run it whenever you
are curious about the various impliciations/conflicts of licenses in your software.

## How To Use

## Licenses Supported (partially)
- GPLv1 (python)
- GPLv2 (python)
- MIT (python)

## Licenses Not Yet Supported
- Apache
- LGPL
- BSD
- MPL
- Zlib-Libpng
- Public Domain
- Artistic License
- GPLv3

If you see one in this list that you really want, adding licenses is really easy. We just haven't gotten around to adding it yet. Feel free to make a pull-request! See the next section for more on how to add a license.

## How To Add Another License

We've tried to make it as easy as possible to add a new license to this project. 
- training/LicenseAttributes.json, and add your desired license to the JSON and its details .

_Rules_
commercialAllowed -> Does this license allow software to be sold commericially?
warrantyGivein 	  -> Does this license explicitly give a warranty?
binaryOnly		  -> Does this license allow the distribution of code in binary-only form?
binaryOnlyIfForce -> Does this license explicitly require code to be released in non-binary form, even if the party is legally obligated not to release the source? (either by another license, court-order, gag-order, etc.)

(Feel free to add another, however, be ready to justify your opinion upon a pull-request.)


## Notes

CenseSense does not have a magical way of figuring out whether code is covered by one license or another, if the license is not included. For this reason,
we always recommend you include the entirety of projects you include in your source-code, and NEVER delete LICENSE files or comments within the code given.

Licenses have all sorts of nuances. Because of this, there are features that are particularly hard to quantify, or have room for legal-interpretation (most of us aren't lawyers),
that make it hard to distinguish the fundemental differences between two licenses, even if there might be in application. This software exists only first-stage filter and shield. 

## The MIT License - Why?

Because the original developer is not a dictator (yet) and he genuinely believes that he has no right to decide arbitrarily what others can and cannot 
copy of his work that he explicility released to the public with no financial/political strings attached. Share this code if you want to, and if you don't want to, that's cool too.
Just have fun. Life is short, and it isn't worth making complicated. 