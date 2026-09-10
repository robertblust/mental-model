# A surface is produced, not exported — design

> `companygraph-export` is one program because its transformation is mechanical. Producing a
> surface is half mechanical and half prose, so this is one script and one procedure, and the
> boundary between them is where judgment starts. This records what the script may resolve,
> what only the surface's own file may decide, and why the output is never committed.

## What the type is for, and what was missing

A surface is a place the company publishes that no script writes. Its file records the rules by
which the model becomes that place: what each unit shows, how the model's facts reach it, and
what the published result must satisfy. The type shipped in core 0.16.0 and the reference
instance holds one, the LinkedIn profile.

Nothing turned those rules into a profile. The file was written to be read by whoever rebuilds
the surface, and rebuilding was six sessions of a person or an agent holding the file open beside
the model and typing. That is the same failure the export skill was built to end, seen from the
other side: a rendering nobody can re-run cheaply is a rendering that will be stale.

**What producing it six times proved is that the file is not the problem.** Reading the file
against the model found nothing across two review rounds. Producing a profile from it found a
missing rule every time — the register was named nowhere, the entries had no order, an experience
with no `organization` had no company, a body had no length — and every one of those was a rule
about what to put in rather than what to leave out. The file was written by somebody deciding
what to omit and it read that way until something tried to use it. So the skill is not only a
convenience: **producing the surface is how a surface file gets checked**, and the check is one
nothing else performs.

## One script and one procedure, and where the line falls

The export makes its case for a single program plainly: one intent implemented twice drifts
apart one rule at a time, and a procedure followed by hand is a different program each time
somebody follows it. Both hold here. Neither makes producing a surface scriptable, because no
script writes a paragraph in a register, chooses which five skills a profile claims, or cuts a
body to the length its period earns.

So the line is not drawn by taste. **Everything a machine can settle is the script's, and the
first thing a machine cannot settle is where the procedure starts.** That line falls in one
place: the script resolves facts, and the surface's file decides what becomes of them.

`facts.py` walks the model once and writes `dist/surfaces/facts.json`:

- Every entity by type, carrying its H1, `kind`, `start`, `end`, `organization`, `url`, its path
  in the model and the text of the sections a body could be written from.
- `organization` resolved, with the fallback the model itself supplies: this instance is a
  company of one, so an experience nobody commissioned or hosted was the company's own work and
  the identity is the answer. Derivable from the model, so the script may do it.
- Dates written in the family's register — a closed en-dash, months abbreviated to three letters
  — because that rule belongs to `conventions/WRITING.md` and not to any surface. It is also the
  rule a produced profile got wrong across twenty-eight ranges before the register was named,
  which is the argument for a script owning it rather than an instruction repeating it.
- The identity's fields, and the profile's sections and its skills table.

**It routes nothing and it orders nothing.** Which kinds reach which unit, and in what order, are
the surface's rules and its file is their only home. A script that knew them would be a second
copy of a rule, which is the condition the whole model exists to end, and the second copy would
be the one nobody reads.

`SKILL.md` carries the procedure. Read the surface entity. Run the script. For each unit its
`## What it shows` names, apply the file's projection rules to the facts and write the unit in
the register the file names. Then hold the result against every constraint the file states, one
at a time, and report each as passed or failed with the evidence measured rather than estimated.

That last step is not bookkeeping. Across six productions the constraint check is what caught two
character limits, a false employer heading and a talk standing above the job it was about, none
of which any other check in the family reaches.

## The output is never committed, and the reason is a rule

`dist/` is gitignored, so `dist/surfaces/` is too, and a produced profile is never a file in this
repository. That is not a convenience of the build directory. R17 says a file in the model
records the rules by which something is made and never the state of the thing made, and a
produced profile is exactly that state. Writing it anywhere the model keeps would break the rule
the surface type rests on.

So the artifact is disposable by design. It is produced, read, pasted and thrown away, and the
next production makes it again from the rules — which is the same claim the vision makes about
every surface, applied to the one artifact that renders a surface.

## What only the file may decide

Stated so a future script does not creep across it. The surface's file alone decides which units
exist, which of the model's facts reach each one, what is left out and why, in what order entries
run, what register the prose takes, and what the published result must satisfy. The script may
resolve a fact, format it the way the family formats every fact, and hand it over. Where the two
would disagree, the file wins and the script has overreached.

The test for a new resolution: could two different surfaces of the same model reasonably want it
different? If yes it is the file's. `organization` falling back to the identity passes — it is
what the model says about that experience, whoever is looking. An order by `end` fails — a CV
might well run by `start`.

## Not done

**A verify script.** The export has one because its output is derivable and comparable; a produced
profile is prose and two correct productions differ. The constraint check in the procedure is
what stands in its place, and it is an agent reading, which is what the constraints were written
for.

**A second surface.** The instance holds one. The script is written against the model rather than
against LinkedIn, so a second should need nothing from it, and that claim is untested until a
second exists.

**A routing declaration in the schema.** It would let the script order and route, and it would
put each rule in a table and in the prose explaining the table. Not while one file can hold it.
