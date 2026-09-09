# Surfaces

One file per surface, written against `meta/core/surface-schema.md` and its writing rules. A
surface has a file here only where no build writes it: blust.ch is written by a build in its
own repository and the skill bundle by `companygraph-export`, so there the script is the
projection and a second copy of its rules would be a copy nothing runs.

A file holds the rules — which of the model's facts reach the surface, in what shape, why
anything is left out and what the published result has to satisfy — and never the surface's own
state. A line saying what a surface shows today is true for a day and nothing here can see it
stop being true (R17); that belongs in the report a validation pass produces.
